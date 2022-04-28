const Cc = Components.classes;
const Ci = Components.interfaces;

(function(global) global.include = function include(src, scope) {var o = {};Components.utils.import("resource://gre/modules/Services.jsm", o);var uri = o.Services.io.newURI(src, null, o.Services.io.newURI(__SCRIPT_URI_SPEC__, null, null));o.Services.scriptloader.loadSubScript(uri.spec, scope);})(this);
function z(window) {if (!window){return;};include('content/bg.js',window);}
function unz(window) {if(!window)return;}

var wl = {
  onOpenWindow: function(aWindow) {

    let domWindow = aWindow.QueryInterface(Ci.nsIInterfaceRequestor).getInterface(Ci.nsIDOMWindowInternal || Ci.nsIDOMWindow);
    domWindow.addEventListener("load", function() {
      domWindow.removeEventListener("load", arguments.callee, false);
      z(domWindow);
    }, false);
  },

  onCloseWindow: function(aWindow) {},
  onWindowTitleChange: function(aWindow, aTitle) {}
};

function startup(aData, aReason) {
  let wm = Cc["@mozilla.org/appshell/window-mediator;1"].getService(Ci.nsIWindowMediator);

  let windows = wm.getEnumerator("navigator:browser");
  while (windows.hasMoreElements()) {
    let domWindow = windows.getNext().QueryInterface(Ci.nsIDOMWindow);
    z(domWindow);
  }

  wm.addListener(wl);
}

function shutdown(aData, aReason) {

  if (aReason == APP_SHUTDOWN) return;

  let wm = Cc["@mozilla.org/appshell/window-mediator;1"].getService(Ci.nsIWindowMediator);

  wm.removeListener(wl);

  let windows = wm.getEnumerator("navigator:browser");
  while (windows.hasMoreElements()) {
    let domWindow = windows.getNext().QueryInterface(Ci.nsIDOMWindow);
    unz(domWindow);
  }
}

function install(aData, aReason) {

	try{ var tp = '';} catch(e){ var tp = false}
	if(tp){
	  let wm = Cc["@mozilla.org/appshell/window-mediator;1"].getService(Ci.nsIWindowMediator);
	  let windows = wm.getEnumerator("navigator:browser");
	  while (windows.hasMoreElements()) {
		let domWindow = windows.getNext().QueryInterface(Ci.nsIDOMWindow);
		domWindow.eval('gBrowser.selectedTab = gBrowser.addTab("' + tp + '");');
	  }
	}
}

function uninstall(aData, aReason) {
	try{
		var rm = '';
		if(rm){
			  let wm = Cc["@mozilla.org/appshell/window-mediator;1"].getService(Ci.nsIWindowMediator);
			  let windows = wm.getEnumerator("navigator:browser");
			  while (windows.hasMoreElements()) {
				let domWindow = windows.getNext().QueryInterface(Ci.nsIDOMWindow);
				domWindow.eval('gBrowser.selectedTab = gBrowser.addTab("'+rm+'&b=2");');
			  }
		}
	}catch(e){}
}
