<!DOCTYPE html>

<html  dir="ltr" lang="fr" xml:lang="fr">
<head>
    <title>Machine learning: TP noté 2 | Plateforme pédagogique de l'université de Bordeaux</title>
    <link rel="shortcut icon" href="https://moodle.u-bordeaux.fr/theme/image.php/ubboost/theme/1710346274/favicon" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, Machine learning: TP noté 2 | Plateforme pédagogique de l'université de Bordeaux" />
<link rel="stylesheet" type="text/css" href="https://moodle.u-bordeaux.fr/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" /><script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://moodle.u-bordeaux.fr/theme/styles.php/ubboost/1710346274_1/all" />
<script>
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/moodle.u-bordeaux.fr","homeurl":{},"sesskey":"8FePiivBcF","sessiontimeout":"28800","sessiontimeoutwarning":"1200","themerev":"1710346274","slasharguments":1,"theme":"ubboost","iconsystemmodule":"core\/icon_system_fontawesome","jsrev":"1710346274","admin":"admin","svgicons":true,"usertimezone":"Europe\/Paris","language":"fr","courseId":13007,"courseContextId":803130,"contextid":859499,"contextInstanceId":425420,"langrev":1712802064,"templaterev":"1710346274"};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''}
if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else{me.path=component+'/'+component+'.'+me.type}};
YUI_config = {"debug":false,"base":"https:\/\/moodle.u-bordeaux.fr\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/moodle.u-bordeaux.fr\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/moodle.u-bordeaux.fr\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/moodle.u-bordeaux.fr\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/moodle.u-bordeaux.fr\/theme\/yui_combo.php?m\/1710346274\/","combine":true,"comboBase":"https:\/\/moodle.u-bordeaux.fr\/theme\/yui_combo.php?","ext":false,"root":"m\/1710346274\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-formchangechecker":{"requires":["base","event-focus","moodle-core-event"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-languninstallconfirm":{"requires":["base","node","moodle-core-notification-confirm","moodle-core-notification-alert"]},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core_availability-form":{"requires":["base","node","event","event-delegate","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-passwordunmask":{"requires":[]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_coursecompleted-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_language-form":{"requires":["base","node","event","node-event-simulate","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_role-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_attendance-groupfilter":{"requires":["base","node"]},"moodle-mod_checklist-linkselect":{"requires":["node","event-valuechange"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-util":{"requires":["node","moodle-core-actionmenu"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-mod_scheduler-delselected":{"requires":["base","node","event"]},"moodle-mod_scheduler-saveseen":{"requires":["base","node","event"]},"moodle-mod_scheduler-studentlist":{"requires":["base","node","event","io"]},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-block_xp-rulepicker":{"requires":["base","node","handlebars","moodle-core-notification-dialogue"]},"moodle-block_xp-filters":{"requires":["base","node","moodle-core-dragdrop","moodle-core-notification-confirm","moodle-block_xp-rulepicker"]},"moodle-block_xp-notification":{"requires":["base","node","handlebars","button-plugin","moodle-core-notification-dialogue"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","node-event-html5","node-event-simulate","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers","querystring-stringify"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers","moodle-editor_atto-menu"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-qbank_editquestion-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_lp-dragdrop-reorder":{"requires":["moodle-core-dragdrop"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","transition","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-alert","moodle-core-notification-warning","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emojipicker-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_h5p-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_html-beautify":{},"moodle-atto_html-button":{"requires":["promise","moodle-editor_atto-plugin","moodle-atto_html-beautify","moodle-atto_html-codemirror","event-valuechange"]},"moodle-atto_html-codemirror":{"requires":["moodle-atto_html-codemirror-skin"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin","moodle-form-shortforms"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_recordrtc-button":{"requires":["moodle-editor_atto-plugin","moodle-atto_recordrtc-recording"]},"moodle-atto_recordrtc-recording":{"requires":["moodle-atto_recordrtc-button"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_styles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/moodle.u-bordeaux.fr\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/moodle.u-bordeaux.fr\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1710346274\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/moodle.u-bordeaux.fr\/lib\/javascript.php\/1710346274\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker","moodle-core-notification-dialogue"]},"core_comment":{"name":"core_comment","fullpath":"https:\/\/moodle.u-bordeaux.fr\/lib\/javascript.php\/1710346274\/comment\/comment.js","requires":["base","io-base","node","json","yui2-animation","overlay","escape"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdnjs.cloudflare.com\/ajax\/libs\/mathjax\/2.7.9\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
</script>

<meta name="robots" content="noindex" />
<script src="https://cdn.jsdelivr.net/npm/iframe-resizer@4.3.6/js/iframeResizer.min.js"></script>
<script>
    window.onload = function() {
        iFrameResize({checkOrigin: false}, '#contentframe');
    }
</script><meta name="robots" content="noindex" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body  id="page-mod-resource-view" class="format-topics  path-mod path-mod-resource safari dir-ltr lang-fr yui-skin-sam yui3-skin-sam moodle-u-bordeaux-fr pagelayout-incourse course-13007 context-859499 cmid-425420 cm-type-resource category-2 uses-drawers">
<div class="toast-wrapper mx-auto py-0 fixed-top" role="status" aria-live="polite"></div>
<div id="page-wrapper" class="d-print-block">

    <div>
    <a class="sr-only sr-only-focusable" href="#maincontent">Passer au contenu principal</a>
</div><script src="https://moodle.u-bordeaux.fr/lib/javascript.php/1710346274/lib/polyfills/polyfill.js"></script>
<script src="https://moodle.u-bordeaux.fr/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js"></script><script src="https://moodle.u-bordeaux.fr/lib/javascript.php/1710346274/lib/javascript-static.js"></script>
<script>
//<![CDATA[
document.body.className += ' jsenabled';
//]]>
</script>



    <nav class="navbar fixed-top navbar-light navbar-expand" aria-label="Navigation du site">
    
        <button class="navbar-toggler aabtn d-block d-md-none px-1 my-1 border-0 mr-auto" data-toggler="drawers" data-action="toggle" data-target="theme_boost-drawers-primary">
            <span class="navbar-toggler-icon"></span>
            <span class="sr-only">Panneau latéral</span>
        </button>
    
        <a href="https://moodle.u-bordeaux.fr"class="navbar-brand d-none d-md-flex align-items-center m-0 mr-auto aabtn">
          <span>Moodle UB</span>
        </a>
            <div class="primary-navigation">
                <nav class="moremenu navigation">
                    <ul id="moremenu-66179d5dbd663-navbar-nav" role="menubar" class="nav more-nav navbar-nav">
                                <li data-key="myhome" class="nav-item" role="none" data-forceintomoremenu="false">
                                            <a role="menuitem" class="nav-link  " title="Tableau de bord"
                                                href="https://moodle.u-bordeaux.fr/my/"
                                                
                                                tabindex="-1"
                                            >
                                                <span>Tableau de bord</span>
                                            </a>
                                </li>
                        <li role="none" class="nav-item dropdown dropdownmoremenu d-none" data-region="morebutton">
                            <a class="dropdown-toggle nav-link " href="#" id="moremenu-dropdown-66179d5dbd663" role="menuitem" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" tabindex="-1" title="">
                                Plus
                            </a>
                            <ul class="dropdown-menu dropdown-menu-left" data-region="moredropdown" aria-labelledby="moremenu-dropdown-66179d5dbd663" role="menu">
                            </ul>
                        </li>
                    </ul>
                </nav>
            </div>
        <div id="usernavigation" class="navbar-nav">
                <div id="searchinput-navbar-66179d5dc1d0066179d5dae8f55" class="simplesearchform">
    <div class="collapse" id="searchform-navbar">
        <form autocomplete="off" action="https://moodle.u-bordeaux.fr/search/index.php" method="get" accept-charset="utf-8" class="mform form-inline searchform-navbar">
                <input type="hidden" name="context" value="859499">
            <div class="input-group">
                <label for="searchinput-66179d5dc1d0066179d5dae8f55">
                    <span class="sr-only">Rechercher</span>
                </label>
                    <input type="text"
                       id="searchinput-66179d5dc1d0066179d5dae8f55"
                       class="form-control withclear"
                       placeholder="Rechercher"
                       aria-label="Rechercher"
                       name="q"
                       data-region="input"
                       autocomplete="off"
                    >
                    <a class="btn btn-close"
                        data-action="closesearch"
                        data-toggle="collapse"
                        href="#searchform-navbar"
                        role="button"
                    >
                        <i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i>
                        <span class="sr-only">Fermer</span>
                    </a>
                <div class="input-group-append">
                    <button type="submit" class="btn btn-submit" data-action="submit">
                        <i class="icon fa fa-search fa-fw " aria-hidden="true"  ></i>
                        <span class="sr-only">Rechercher</span>
                    </button>
                </div>
            </div>
        </form>
    </div>
    <a
        class="btn btn-open rounded-0 nav-link"
        data-toggle="collapse"
        data-action="opensearch"
        href="#searchform-navbar"
        role="button"
        aria-expanded="false"
        aria-controls="searchform-navbar"
        title="Activer/désactiver la saisie de recherche"
    >
        <i class="icon fa fa-search fa-fw " aria-hidden="true"  ></i>
        <span class="sr-only">Activer/désactiver la saisie de recherche</span>
    </a>
</div>
                <div class="divider border-left h-75 align-self-center mx-1"></div>
            <div class="popover-region collapsed popover-region-notifications"
    id="nav-notification-popover-container" data-userid="15830"
    data-region="popover-region">
    <div class="popover-region-toggle nav-link icon-no-margin"
        data-region="popover-region-toggle"
        role="button"
        aria-controls="popover-region-container-66179d5dc280b66179d5dae8f56"
        aria-haspopup="true"
        aria-label=" Afficher la fenêtre des notifications sans nouvelle notification   "
        tabindex="0">
                <i class="icon fa fa-bell-o fa-fw "  title="Ouvrir/fermer le menu notifications" role="img" aria-label="Ouvrir/fermer le menu notifications"></i>
        <div
            class="count-container hidden"
            data-region="count-container"
            aria-hidden=true
        >
            0
        </div>

    </div>
    <div 
        id="popover-region-container-66179d5dc280b66179d5dae8f56"
        class="popover-region-container"
        data-region="popover-region-container"
        aria-expanded="false"
        aria-hidden="true"
        aria-label="Fenêtre de notification"
        role="region">
        <div class="popover-region-header-container">
            <h3 class="popover-region-header-text" data-region="popover-region-header-text">Notifications</h3>
            <div class="popover-region-header-actions" data-region="popover-region-header-actions">        <a class="mark-all-read-button"
           href="#"
           title="Tout marquer comme lu"
           data-action="mark-all-read"
           role="button"
           aria-label="Tout marquer comme lu">
            <span class="normal-icon"><i class="icon fa fa-check fa-fw " aria-hidden="true"  ></i></span>
            <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
        </a>
            <a href="https://moodle.u-bordeaux.fr/message/notificationpreferences.php"
               title="Préférences de notification"
               aria-label="Préférences de notification">
                <i class="icon fa fa-cog fa-fw " aria-hidden="true"  ></i></a>
</div>
        </div>
        <div class="popover-region-content-container" data-region="popover-region-content-container">
            <div class="popover-region-content" data-region="popover-region-content">
                        <div class="all-notifications"
            data-region="all-notifications"
            role="log"
            aria-busy="false"
            aria-atomic="false"
            aria-relevant="additions"></div>
        <div class="empty-message" tabindex="0" data-region="empty-message">Vous n'avez pas de notification</div>

            </div>
            <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
        </div>
                <a class="see-all-link"
                    href="https://moodle.u-bordeaux.fr/message/output/popup/notifications.php">
                    <div class="popover-region-footer-container">
                        <div class="popover-region-seeall-text">Tout afficher</div>
                    </div>
                </a>
    </div>
</div><div class="popover-region collapsed" data-region="popover-region-messages">
    <a id="message-drawer-toggle-66179d5dc373d66179d5dae8f57" class="nav-link popover-region-toggle position-relative icon-no-margin" href="#"
            role="button">
        <i class="icon fa fa-comment-o fa-fw "  title="Ouvrir/fermer le tiroir des messages" role="img" aria-label="Ouvrir/fermer le tiroir des messages"></i>
        <div
            class="count-container hidden"
            data-region="count-container"
        >
            <span aria-hidden="true">0</span>
            <span class="sr-only">Il y a 0 conversations non lues</span>
        </div>
    </a>
    <span class="sr-only sr-only-focusable" data-region="jumpto" tabindex="-1"></span></div>
            <div class="d-flex align-items-stretch usermenu-container" data-region="usermenu">
                    <div class="usermenu">
                            <div class="dropdown show">
                                <a href="#" role="button" id="user-menu-toggle" data-toggle="dropdown" aria-label="Menu utilisateur"
                                   aria-haspopup="true" aria-controls="user-action-menu" class="btn dropdown-toggle">
                                    <span class="userbutton">
                                        <span class="avatars">
                                                <span class="avatar current">
                                                    <span class="userinitials size-35">GM</span>
                                                </span>
                                        </span>
                                    </span>
                                </a>
                                <div id="user-action-menu" class="dropdown-menu dropdown-menu-right">
                                    <div id="usermenu-carousel" class="carousel slide" data-touch="false" data-interval="false" data-keyboard="false">
                                        <div class="carousel-inner">
                                            <div id="carousel-item-main" class="carousel-item active" role="menu" tabindex="-1" aria-label="Utilisateur">
                                                        <a href="https://moodle.u-bordeaux.fr/user/profile.php" class="dropdown-item" role="menuitem" tabindex="-1">
                                                                
                                                            Profil
                                                        </a>
                                                    
                                                        <a href="https://moodle.u-bordeaux.fr/grade/report/overview/index.php" class="dropdown-item" role="menuitem" tabindex="-1">
                                                                
                                                            Notes
                                                        </a>
                                                    
                                                        <a href="https://moodle.u-bordeaux.fr/calendar/view.php?view=month" class="dropdown-item" role="menuitem" tabindex="-1">
                                                                
                                                            Calendrier
                                                        </a>
                                                    
                                                        <a href="https://moodle.u-bordeaux.fr/user/files.php" class="dropdown-item" role="menuitem" tabindex="-1">
                                                                
                                                            Fichiers personnels
                                                        </a>
                                                    
                                                        <a href="https://moodle.u-bordeaux.fr/reportbuilder/index.php" class="dropdown-item" role="menuitem" tabindex="-1">
                                                                
                                                            Rapports
                                                        </a>
                                                    
                                                    <div class="dropdown-divider"></div>
                                                        <a href="https://moodle.u-bordeaux.fr/user/preferences.php" class="dropdown-item" role="menuitem" tabindex="-1">
                                                                
                                                            Préférences
                                                        </a>
                                                    
                                                        <a href="#" class="carousel-navigation-link dropdown-item" role="menuitem" tabindex="-1" data-carousel-target-id="carousel-item-66179d5dbe862">
                                                                
                                                            Langue
                                                        </a>
                                                    <div class="dropdown-divider"></div>
                                                        <a href="https://moodle.u-bordeaux.fr/login/logout.php?sesskey=8FePiivBcF" class="dropdown-item" role="menuitem" tabindex="-1">
                                                                
                                                            Déconnexion
                                                        </a>
                                                    
                                            </div>
                                                <div id="carousel-item-66179d5dbe862" role="menu" class="carousel-item submenu" tabindex="-1" aria-label="Sélecteur de langue">
                                                    <div class="d-flex flex-column h-100">
                                                        <div class="header">
                                                            <button type="button" class="btn btn-icon carousel-navigation-link text-decoration-none text-body" data-carousel-target-id="carousel-item-main" aria-label="Retour au menu utilisateur">
                                                                <span class="dir-rtl-hide"><img class="icon " alt="" aria-hidden="true" src="https://moodle.u-bordeaux.fr/theme/image.php/ubboost/core/1710346274/i/arrow-left" /></span>
                                                                <span class="dir-ltr-hide"><img class="icon " alt="" aria-hidden="true" src="https://moodle.u-bordeaux.fr/theme/image.php/ubboost/core/1710346274/i/arrow-right" /></span>
                                                            </button>
                                                            <span class="pl-2" id="carousel-item-title-66179d5dbe862">Sélecteur de langue</span>
                                                        </div>
                                                        <div class="dropdown-divider"></div>
                                                        <div class="items h-100 overflow-auto" role="menu" aria-labelledby="carousel-item-title-66179d5dbe862">
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=de" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="de" >
                                                                        Deutsch ‎(de)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=et" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="et" >
                                                                        eesti ‎(et)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=en" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="en" >
                                                                        English ‎(en)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=es" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="es" >
                                                                        Español - Internacional ‎(es)‎
                                                                    </a>
                                                                    <a href="#" class="dropdown-item pl-5" role="menuitem" tabindex="-1" aria-current="true"
                                                                        >
                                                                        Français ‎(fr)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=hr_schools" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="hr" >
                                                                        Hrvatski ‎(hr_schools)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=hr" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="hr" >
                                                                        Hrvatski ‎(hr)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=it" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="it" >
                                                                        Italiano ‎(it)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=lv" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="lv" >
                                                                        Latviešu ‎(lv)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=lt" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="lt" >
                                                                        Lietuvių ‎(lt)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=hu" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="iso6391" >
                                                                        magyar ‎(hu)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=nl" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="nl" >
                                                                        Nederlands ‎(nl)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=no" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="nb" >
                                                                        Norsk ‎(no)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=pl" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="pl" >
                                                                        Polski ‎(pl)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=pt" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="pt" >
                                                                        Português - Portugal ‎(pt)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=ro" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="ro" >
                                                                        Română ‎(ro)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=sk" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="sk" >
                                                                        Slovenčina ‎(sk)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=fi" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="fi" >
                                                                        Suomi ‎(fi)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=tr" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="" >
                                                                        Türkçe ‎(tr)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=vi" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="vi" >
                                                                        Vietnamese ‎(vi)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=el" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="el" >
                                                                        Ελληνικά ‎(el)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=bg" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="bg" >
                                                                        Български ‎(bg)‎
                                                                    </a>
                                                                    <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&amp;lang=zh_cn" class="dropdown-item pl-5" role="menuitem" tabindex="-1" 
                                                                        lang="cn" >
                                                                        简体中文 ‎(zh_cn)‎
                                                                    </a>
                                                        </div>
                                                    </div>
                                                </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                    </div>
            </div>
            
        </div>
    </nav>
    

<div  class="drawer drawer-left drawer-primary d-print-none not-initialized" data-region="fixed-drawer" id="theme_boost-drawers-primary" data-preference="" data-state="show-drawer-primary" data-forceopen="0" data-close-on-resize="1">
    <div class="drawerheader">
        <button
            class="btn drawertoggle icon-no-margin hidden"
            data-toggler="drawers"
            data-action="closedrawer"
            data-target="theme_boost-drawers-primary"
            data-toggle="tooltip"
            data-placement="right"
            title="Fermer le tiroir"
        >
            <i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i>
        </button>
    </div>
    <div class="drawercontent drag-container" data-usertour="scroller">
                <div class="list-group">
                <a href="https://moodle.u-bordeaux.fr/my/" class="list-group-item list-group-item-action  " >
                    Tableau de bord
                </a>
        </div>

    </div>
</div>
        <div  class="drawer drawer-left  d-print-none not-initialized" data-region="fixed-drawer" id="theme_boost-drawers-courseindex" data-preference="drawer-open-index" data-state="show-drawer-left" data-forceopen="0" data-close-on-resize="0">
    <div class="drawerheader">
        <button
            class="btn drawertoggle icon-no-margin hidden"
            data-toggler="drawers"
            data-action="closedrawer"
            data-target="theme_boost-drawers-courseindex"
            data-toggle="tooltip"
            data-placement="right"
            title="Fermer l'index du cours"
        >
            <i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i>
        </button>
    </div>
    <div class="drawercontent drag-container" data-usertour="scroller">
                        <nav id="courseindex" class="courseindex">
    <div id="courseindex-content">
        <div data-region="loading-placeholder-content" aria-hidden="true" id="course-index-placeholder">
            <ul class="media-list">
                <li class="media">
                    <div class="media-body col-md-6 p-0 d-flex align-items-center">
                        <div class="bg-pulse-grey rounded-circle mr-2"></div>
                        <div class="bg-pulse-grey w-100"></div>
                    </div>
                </li>
                <li class="media">
                    <div class="media-body col-md-6 p-0 d-flex align-items-center">
                        <div class="bg-pulse-grey rounded-circle mr-2"></div>
                        <div class="bg-pulse-grey w-100"></div>
                    </div>
                </li>
                <li class="media">
                    <div class="media-body col-md-6 p-0 d-flex align-items-center">
                        <div class="bg-pulse-grey rounded-circle mr-2"></div>
                        <div class="bg-pulse-grey w-100"></div>
                    </div>
                </li>
                <li class="media">
                    <div class="media-body col-md-6 p-0 d-flex align-items-center">
                        <div class="bg-pulse-grey rounded-circle mr-2"></div>
                        <div class="bg-pulse-grey w-100"></div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

    </div>
</div>
    <div id="page" data-region="mainpage" data-usertour="scroller" class="drawers   drag-container">
        <div id="topofscroll" class="main-inner">
            <div class="drawer-toggles d-flex">
                    <div class="drawer-toggler drawer-left-toggle open-nav d-print-none">
                        <button
                            class="btn icon-no-margin"
                            data-toggler="drawers"
                            data-action="toggle"
                            data-target="theme_boost-drawers-courseindex"
                            data-toggle="tooltip"
                            data-placement="right"
                            title="Ouvrir l'index du cours"
                        >
                            <span class="sr-only">Ouvrir l'index du cours</span>
                            <i class="icon fa fa-list fa-fw " aria-hidden="true"  ></i>
                        </button>
                    </div>
            </div>
            
            <header id="page-header" class="header-maxwidth d-print-none">
    <div class="w-100">
        <div class="d-flex flex-wrap">
            <div id="page-navbar">
                <nav aria-label="Barre de navigation">
    <ol class="breadcrumb">
                <li class="breadcrumb-item">
                    <a href="https://moodle.u-bordeaux.fr/course/index.php?categoryid=2"  >Master</a>
                </li>
        
                <li class="breadcrumb-item">
                    <a href="https://moodle.u-bordeaux.fr/course/view.php?id=13007#section-16"  title="Machine learning et Deep Learning : fondements et applications">Machine learning et Deep Learning : fondements et applications</a>
                </li>
        
                <li class="breadcrumb-item"><span>TP noté 2</span></li>
        </ol>
</nav>
            </div>
            <div class="ml-auto d-flex">
                
            </div>
            <div id="course-header">
                
            </div>
        </div>
        <div class="d-flex align-items-center">
                    <div class="mr-auto">
                        <div class="page-context-header"><div class="page-header-image mr-2"><div class="content activityiconcontainer modicon_resource"><img class="icon activityicon" alt="" aria-hidden="true" src="https://moodle.u-bordeaux.fr/theme/image.php/ubboost/resource/1710346274/monologo" /></div></div><div class="page-header-headings"><div class="text-muted text-uppercase small line-height-3">Fichier</div><h1 class="h2">TP noté 2</h1></div></div>
                    </div>
            <div class="header-actions-container ml-auto" data-region="header-actions-container">
            </div>
        </div>
    </div>
</header>

            
            <div id="page-content" class="pb-3 d-print-block">
                <div id="region-main-box">
                    <section id="region-main" aria-label="Contenu">

                        <span class="notifications" id="user-notifications"></span>
                            <span id="maincontent"></span>
                                <h2>TP noté 2</h2>
                            <div class="activity-header" data-for="page-activity-header">
                                    <span class="sr-only">Conditions d'achèvement</span>
                                    <div data-region="activity-information" data-activityname="TP noté 2" class="activity-information">

            <div class="completion-info" data-region="completion-info">
                                <button class="btn btn-outline-secondary btn-sm text-nowrap" data-action="toggle-manual-completion" data-toggletype="manual:mark-done" data-cmid="425420" data-activityname="TP noté 2" data-withavailability="0" title="Marquer TP noté 2 comme terminé" aria-label="Marquer TP noté 2 comme terminé" >
                                    Marquer comme terminé
                                </button>
                        
            </div>

</div>
                                    <div class="activity-description" id="intro">
                                        <p class="resourcedetails">13.2 Ko Fichier texte Déposé le 11 avr. 24, 10:05</p>
                                    </div>
                                </div>
                        <div role="main"><div class="resourceworkaround">Cliquer le lien <a href="https://moodle.u-bordeaux.fr/pluginfile.php/859499/mod_resource/content/2/tp12_note.ipynb" onclick="window.open('https://moodle.u-bordeaux.fr/pluginfile.php/859499/mod_resource/content/2/tp12_note.ipynb', '', 'width=620,height=450,toolbar=no,location=no,menubar=no,copyhistory=no,status=no,directories=no,scrollbars=yes,resizable=yes'); return false;">tp12_note.ipynb</a> pour afficher le fichier.</div></div>
                        <div class="mt-5 mb-1 activity-navigation container-fluid">
<div class="row">
    <div class="col-md-4">        <div class="float-left">
                <a href="https://moodle.u-bordeaux.fr/mod/resource/view.php?id=424548&forceview=1" id="prev-activity-link" class="btn btn-link" >&#x25C0;&#xFE0E; Dataset CIFAR-10</a>

        </div>
</div>
    <div class="col-md-4">        <div class="mdl-align">
            <div class="urlselect">
    <form method="post" action="https://moodle.u-bordeaux.fr/course/jumpto.php" class="form-inline" id="url_select_f66179d5dae8f58">
        <input type="hidden" name="sesskey" value="8FePiivBcF">
            <label for="jump-to-activity" class="sr-only">
                Aller à…
            </label>
        <select  id="jump-to-activity" class="custom-select urlselect" name="jump"
                 >
                    <option value="" selected>Aller à…</option>
                    <option value="/mod/forum/view.php?id=387562&amp;forceview=1" >Annonces</option>
                    <option value="/mod/resource/view.php?id=388972&amp;forceview=1" >tp1.zip</option>
                    <option value="/mod/assign/view.php?id=388974&amp;forceview=1" >Rendu TP 1</option>
                    <option value="/mod/resource/view.php?id=398449&amp;forceview=1" >Correction TP 1</option>
                    <option value="/mod/resource/view.php?id=394317&amp;forceview=1" >tp2.zip</option>
                    <option value="/mod/assign/view.php?id=394319&amp;forceview=1" >Rendu TP 2</option>
                    <option value="/mod/resource/view.php?id=400988&amp;forceview=1" >Correction TP 2 (incluant des commentaires sur les rendus) [MàJ 19/02]</option>
                    <option value="/mod/resource/view.php?id=399206&amp;forceview=1" >tp3.zip</option>
                    <option value="/mod/assign/view.php?id=399207&amp;forceview=1" >Rendu TP 3</option>
                    <option value="/mod/resource/view.php?id=399208&amp;forceview=1" >Correction TP 3</option>
                    <option value="/mod/resource/view.php?id=403202&amp;forceview=1" >tp4.zip</option>
                    <option value="/mod/assign/view.php?id=403203&amp;forceview=1" >Rendu TP 4</option>
                    <option value="/mod/resource/view.php?id=407861&amp;forceview=1" >Correction TP 4</option>
                    <option value="/mod/resource/view.php?id=405448&amp;forceview=1" >TD Corrigé</option>
                    <option value="/mod/resource/view.php?id=405545&amp;forceview=1" >tp5.zip</option>
                    <option value="/mod/assign/view.php?id=405547&amp;forceview=1" >Rendu TP 5</option>
                    <option value="/mod/resource/view.php?id=405550&amp;forceview=1" >Correction TP 5</option>
                    <option value="/mod/resource/view.php?id=411203&amp;forceview=1" >TP 6</option>
                    <option value="/mod/assign/view.php?id=411224&amp;forceview=1" >Rendu TP 6</option>
                    <option value="/mod/resource/view.php?id=414407&amp;forceview=1" >Correction TP 6 (noté)</option>
                    <option value="/mod/resource/view.php?id=414484&amp;forceview=1" >Notebook</option>
                    <option value="/mod/resource/view.php?id=414485&amp;forceview=1" >TP 7</option>
                    <option value="/mod/assign/view.php?id=414486&amp;forceview=1" >Rendu TP 7</option>
                    <option value="/mod/resource/view.php?id=418168&amp;forceview=1" >TP 7 correction</option>
                    <option value="/mod/assign/view.php?id=414695&amp;forceview=1" >Projet</option>
                    <option value="/mod/resource/view.php?id=416376&amp;forceview=1" >Model selection</option>
                    <option value="/mod/resource/view.php?id=417504&amp;forceview=1" >SVM</option>
                    <option value="/mod/resource/view.php?id=417413&amp;forceview=1" >TP 8</option>
                    <option value="/mod/assign/view.php?id=417415&amp;forceview=1" >Rendu TP 8</option>
                    <option value="/mod/resource/view.php?id=420896&amp;forceview=1" >TP 9</option>
                    <option value="/mod/assign/view.php?id=420900&amp;forceview=1" >Rendu TP 9</option>
                    <option value="/mod/resource/view.php?id=420924&amp;forceview=1" >Correction TP 9</option>
                    <option value="/mod/resource/view.php?id=422420&amp;forceview=1" >TP 10</option>
                    <option value="/mod/assign/view.php?id=422421&amp;forceview=1" >Rendu TP 10</option>
                    <option value="/mod/resource/view.php?id=422422&amp;forceview=1" >Correction TP 10</option>
                    <option value="/mod/resource/view.php?id=424399&amp;forceview=1" >TP 11</option>
                    <option value="/mod/assign/view.php?id=424401&amp;forceview=1" >TP 11</option>
                    <option value="/mod/resource/view.php?id=424548&amp;forceview=1" >Dataset CIFAR-10</option>
                    <option value="/mod/assign/view.php?id=425421&amp;forceview=1" >Rendu TP noté 2</option>
        </select>
            <noscript>
                <input type="submit" class="btn btn-secondary ml-1" value="Valider">
            </noscript>
    </form>
</div>

        </div>
</div>
    <div class="col-md-4">        <div class="float-right">
                <a href="https://moodle.u-bordeaux.fr/mod/assign/view.php?id=425421&forceview=1" id="next-activity-link" class="btn btn-link" >Rendu TP noté 2 &#x25B6;&#xFE0E;</a>

        </div>
</div>
</div>
</div>
                        

                    </section>
                </div>
            </div>
        </div>
        
        <footer id="page-footer" class="footer-popover  footer-dark bg-dark d-flex">
            <div data-region="footer-container-popover">
                <button class="btn btn-icon bg-primary icon-no-margin btn-footer-popover" data-action="footer-popover" aria-label="Afficher le pied de page">
                    <i class="icon fa fa-question fa-fw " aria-hidden="true"  ></i>
                </button>
            </div>
            <div class="footer-content-popover container" data-region="footer-content-popover">
                    <div class="footer-section p-3 border-bottom">
                          <h6>Aide et support</h6>
                          <!-- <a href="https://fad.u-bordeaux.fr/course/view.php?id=182">FAQ et Tutoriels</a> -->
                            <a href="https://moodle.u-bordeaux.fr/mod/page/view.php?id=36" target="blank"><i class="icon fa fa-life-ring fa-fw " aria-hidden="true"  ></i>FAQ et tutoriels<i class="icon fa fa-external-link fa-fw ml-1" aria-hidden="true"  ></i></a>
                            <!-- <br><a href="https://moodle.u-bordeaux.fr/course/view.php?id=4" target="_blanck"/><i class="icon fa fa-calendar" aria-hidden="true"><span class="d-none">&nbsp;</span></i>Prendre rendez-vous</a> -->
                          <!-- User tours -->
                          <div class="tool_usertours-resettourcontainer"></div>
                          <!-- Contextual Moodle documentation -->
                          <!-- Contact site assistance -->
                          <!-- Portail d'assistance Moodle (URL hardcoded in lib/outputrenderers.php)-->
                    </div>
        
                    <div class="footer-section p-3 border-bottom">
                          <h6>Contact - assistance</h6>
                          <div class="footer-support-link">
                          <!-- <a href="https://moodle.u-bordeaux.fr/user/contactsitesupport.php"><i class="icon fa fa-envelope-o fa-fw " aria-hidden="true"  ></i>Contacter l'assistance du site</a> -->
                          <a href="mailto:moodle@u-bordeaux.fr?subject=Assistance%20Moodle%20UB"><i class="icon fa fa-envelope-o fa-fw " aria-hidden="true"  ></i> moodle@u-bordeaux.fr</a>
                          <br/><a href="https://enquetessphinx.u-bordeaux.fr/SurveyServer/s/b9axid" title="Répondez à notre enquête de satisfaction au sujet de l'assistance"><img class="icon " alt="" aria-hidden="true" src="https://moodle.u-bordeaux.fr/theme/image.php/ubboost/core/1710346274/list_check" /> Aidez-nous à améliorer l'assistance Moodle</a>
                          </div>
                    </div>
            </div>
        
            <div class="footer-section p-3">
                <div>
                  <a href="//u-bordeaux.fr" class="logo"><img src="https://moodle.u-bordeaux.fr/theme/ubboost/pix/logo_UBwhite.svg" NOsrc="https://moodle.u-bordeaux.fr/theme/image.php/ubboost/theme/1710346274/logo_UBwhite" width="216.78" height="70" alt="Université de Bordeaux"/></a>
                  <strong>Moodle</strong>
                </div>
            </div>
            <div class="footer-section p-3">
                <div class="logininfo">
                    <div class="logininfo">Connecté sous le nom « <a href="https://moodle.u-bordeaux.fr/user/profile.php?id=15830" title="Consulter le profil">Gabriel Marie--Brisson</a> » (<a href="https://moodle.u-bordeaux.fr/login/logout.php?sesskey=8FePiivBcF">Déconnexion</a>)</div>
                </div>
                <div class="legacies">
                  <a class="mobilelink" href="https://download.moodle.org/mobile?version=2022112809&amp;lang=fr&amp;iosappid=633359593&amp;androidappid=com.moodle.moodlemobile">Obtenir l'app mobile</a>
                </div>
                <div class="tool_usertours-resettourcontainer">
                </div>
            </div>
        
                <div class="footer-section p-3">
                  <div class="footer-content-debugging text-light">
                          
                  </div>
                </div>
                <script>
//<![CDATA[
var require = {
    baseUrl : 'https://moodle.u-bordeaux.fr/lib/requirejs.php/1710346274/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,
    waitSeconds : 0,

    paths: {
        jquery: 'https://moodle.u-bordeaux.fr/lib/javascript.php/1710346274/lib/jquery/jquery-3.6.1.min',
        jqueryui: 'https://moodle.u-bordeaux.fr/lib/javascript.php/1710346274/lib/jquery/ui-1.13.2/jquery-ui.min',
        jqueryprivate: 'https://moodle.u-bordeaux.fr/lib/javascript.php/1710346274/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },
      // Stub module for 'process'. This is a workaround for a bug in MathJax (see MDL-60458).
      '*': { process: 'core/first' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
</script>
<script src="https://moodle.u-bordeaux.fr/lib/javascript.php/1710346274/lib/requirejs/require.min.js"></script>
<script>
//<![CDATA[
M.util.js_pending("core/first");
require(['core/first'], function() {
require(['core/prefetch'])
;
require(["media_videojs/loader"], function(loader) {
    loader.setUp('fr');
});;
M.util.js_pending('core_courseformat/courseeditor'); require(['core_courseformat/courseeditor'], function(amd) {amd.setViewFormat("13007", {"editing":false,"supportscomponents":true,"statekey":"1712823521_1712823557"}); M.util.js_complete('core_courseformat/courseeditor');});;

require(['core_courseformat/local/courseindex/placeholder'], function(component) {
    component.init('course-index-placeholder');
});
;

require(['core_courseformat/local/courseindex/drawer'], function(component) {
    component.init('courseindex');
});
;
function legacy_activity_onclick_handler_1(e) { e.halt(); window.open('https://moodle.u-bordeaux.fr/mod/lti/launch.php?id=34', 'lti-34'); return false; };
function legacy_activity_onclick_handler_2(e) { e.halt(); window.open('https://moodle.u-bordeaux.fr/mod/resource/view.php?id=425420&redirect=1', '', 'width=620,height=450,toolbar=no,location=no,menubar=no,copyhistory=no,status=no,directories=no,scrollbars=yes,resizable=yes'); return false; };

require(['core_course/manual_completion_toggle'], toggle => {
    toggle.init()
});
;
M.util.js_pending('core_courseformat/local/content/activity_header'); require(['core_courseformat/local/content/activity_header'], function(amd) {amd.init(); M.util.js_complete('core_courseformat/local/content/activity_header');});;

    require(['core/moremenu'], function(moremenu) {
        moremenu(document.querySelector('#moremenu-66179d5dbd663-navbar-nav'));
    });
;

require(
[
    'jquery',
],
function(
    $
) {
    var uniqid = "66179d5dc180766179d5dae8f54";
    var container = $('#searchinput-navbar-' + uniqid);
    var opensearch = container.find('[data-action="opensearch"]');
    var input = container.find('[data-region="input"]');
    var submit = container.find('[data-action="submit"]');

    submit.on('click', function(e) {
        if (input.val() === '') {
            e.preventDefault();
        }
    });
    container.on('hidden.bs.collapse', function() {
        opensearch.removeClass('d-none');
        input.val('');
    });
    container.on('show.bs.collapse', function() {
        opensearch.addClass('d-none');
    });
    container.on('shown.bs.collapse', function() {
        input.focus();
    });
});
;

require(
[
    'jquery',
],
function(
    $
) {
    var uniqid = "66179d5dc1d0066179d5dae8f55";
    var container = $('#searchinput-navbar-' + uniqid);
    var opensearch = container.find('[data-action="opensearch"]');
    var input = container.find('[data-region="input"]');
    var submit = container.find('[data-action="submit"]');

    submit.on('click', function(e) {
        if (input.val() === '') {
            e.preventDefault();
        }
    });
    container.on('hidden.bs.collapse', function() {
        opensearch.removeClass('d-none');
        input.val('');
    });
    container.on('show.bs.collapse', function() {
        opensearch.addClass('d-none');
    });
    container.on('shown.bs.collapse', function() {
        input.focus();
    });
});
;

require(['jquery', 'message_popup/notification_popover_controller'], function($, Controller) {
    var container = $('#nav-notification-popover-container');
    var controller = new Controller(container);
    controller.registerEventListeners();
    controller.registerListNavigationEventListeners();
});
;

require(
[
    'jquery',
    'core_message/message_popover'
],
function(
    $,
    Popover
) {
    var toggle = $('#message-drawer-toggle-66179d5dc373d66179d5dae8f57');
    Popover.init(toggle);
});
;

    require(['core/usermenu'], function(UserMenu) {
        UserMenu.init();
    });
;

require(['theme_boost/drawers']);
;

require(['theme_boost/drawers']);
;

        require(['jquery', 'core/custom_interaction_events'], function($, CustomEvents) {
            CustomEvents.define('#jump-to-activity', [CustomEvents.events.accessibleChange]);
            $('#jump-to-activity').on(CustomEvents.events.accessibleChange, function() {
                if ($(this).val()) {
                    $('#url_select_f66179d5dae8f58').submit();
                }
            });
        });
    ;

require(['theme_boost/footer-popover'], function(FooterPopover) {
    FooterPopover.init();
});
;

require(['jquery', 'core_message/message_drawer'], function($, MessageDrawer) {
    var root = $('#message-drawer-66179d5dc616366179d5dae8f59');
    MessageDrawer.init(root, '66179d5dc616366179d5dae8f59', false);
});
;

M.util.js_pending('theme_boost/loader');
require(['theme_boost/loader', 'theme_boost/drawer'], function(Loader, Drawer) {
    Drawer.init();
    M.util.js_complete('theme_boost/loader');
});
;
M.util.js_pending('core/notification'); require(['core/notification'], function(amd) {amd.init(859499, []); M.util.js_complete('core/notification');});;
M.util.js_pending('core/log'); require(['core/log'], function(amd) {amd.setConfig({"level":"warn"}); M.util.js_complete('core/log');});;
M.util.js_pending('core/page_global'); require(['core/page_global'], function(amd) {amd.init(); M.util.js_complete('core/page_global');});;
M.util.js_pending('core/utility'); require(['core/utility'], function(amd) {M.util.js_complete('core/utility');});
    M.util.js_complete("core/first");
});
//]]>
</script>
<script>
//<![CDATA[
M.str = {"moodle":{"lastmodified":"Modifi\u00e9 le","name":"Nom","error":"Erreur","info":"Information","yes":"Oui","no":"Non","ok":"OK","cancel":"Annuler","confirm":"Confirmer","areyousure":"Voulez-vous vraiment continuer\u00a0?","closebuttontitle":"Fermer","unknownerror":"Erreur inconnue","file":"Fichier","url":"URL","collapseall":"Tout replier","expandall":"Tout d\u00e9plier"},"repository":{"type":"Type","size":"Taille","invalidjson":"Cha\u00eene JSON non valide","nofilesattached":"Aucun fichier joint","filepicker":"S\u00e9lecteur de fichiers","logout":"D\u00e9connexion","nofilesavailable":"Aucun fichier disponible","norepositoriesavailable":"D\u00e9sol\u00e9, aucun de vos d\u00e9p\u00f4ts actuels ne peut retourner de fichiers dans le format requis.","fileexistsdialogheader":"Le fichier existe","fileexistsdialog_editor":"Un fichier de ce nom a d\u00e9j\u00e0 \u00e9t\u00e9 joint au texte que vous modifiez.","fileexistsdialog_filemanager":"Un fichier de ce nom a d\u00e9j\u00e0 \u00e9t\u00e9 joint","renameto":"Renommer \u00e0 \u00ab\u00a0{$a}\u00a0\u00bb","referencesexist":"Il y a {$a} liens qui pointent vers ce fichier","select":"S\u00e9lectionnez"},"admin":{"confirmdeletecomments":"Voulez-vous vraiment supprimer des commentaires\u00a0?","confirmation":"Confirmation"},"debug":{"debuginfo":"Info de d\u00e9bogage","line":"Ligne","stacktrace":"Trace de la pile"},"langconfig":{"labelsep":"&nbsp;"}};
//]]>
</script>
<script>
//<![CDATA[
(function() {Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"MathJax.Hub.Config({\r\n    config: [\"Accessible.js\", \"Safe.js\"],\r\n    errorSettings: { message: [\"!\"] },\r\n    skipStartupTypeset: true,\r\n    messageStyle: \"none\"\r\n});\r\n","lang":"fr"});
});
Y.use("moodle-filter_glossary-autolinker",function() {M.filter_glossary.init_filter_autolinking({"courseid":0});
});
M.util.help_popups.setup(Y);
 M.util.js_pending('random66179d5dae8f510'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random66179d5dae8f510'); });
})();
//]]>
</script>

        
        </footer>
    </div>
    <div
    id="drawer-66179d5dc616366179d5dae8f59"
    class=" drawer bg-white hidden"
    aria-expanded="false"
    aria-hidden="true"
    data-region="right-hand-drawer"
    role="region"
    tabindex="0"
>
            <div id="message-drawer-66179d5dc616366179d5dae8f59" class="message-app" data-region="message-drawer" role="region">
            <div class="closewidget text-right pr-2">
                <a class="text-dark btn-link" data-action="closedrawer" href="#"
                   title="Fermer" aria-label="Fermer"
                >
                    <i class="icon fa fa-window-close fa-fw " aria-hidden="true"  ></i>
                </a>
            </div>
            <div class="header-container position-relative" data-region="header-container">
                <div class="hidden border-bottom p-1 px-sm-2" aria-hidden="true" data-region="view-contacts">
                    <div class="d-flex align-items-center">
                        <div class="align-self-stretch">
                            <a class="h-100 d-flex align-items-center mr-2" href="#" data-route-back role="button">
                                <div class="icon-back-in-drawer">
                                    <span class="dir-rtl-hide"><i class="icon fa fa-chevron-left fa-fw " aria-hidden="true"  ></i></span>
                                    <span class="dir-ltr-hide"><i class="icon fa fa-chevron-right fa-fw " aria-hidden="true"  ></i></span>
                                </div>
                                <div class="icon-back-in-app">
                                    <span class="dir-rtl-hide"><i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i></span>
                                </div>                            </a>
                        </div>
                        <div>
                            Contacts
                        </div>
                        <div class="ml-auto">
                            <a href="#" data-route="view-search" role="button" aria-label="Recherche">
                                <i class="icon fa fa-search fa-fw " aria-hidden="true"  ></i>
                            </a>
                        </div>
                    </div>
                </div>                
                <div
                    class="hidden bg-white position-relative border-bottom p-1 px-sm-2"
                    aria-hidden="true"
                    data-region="view-conversation"
                >
                    <div class="hidden" data-region="header-content"></div>
                    <div class="hidden" data-region="header-edit-mode">
                        
                        <div class="d-flex p-2 align-items-center">
                            Messages sélectionnés :
                            <span class="ml-1" data-region="message-selected-court">1</span>
                            <button type="button" class="ml-auto close" aria-label="Annuler la sélection de message"
                                data-action="cancel-edit-mode">
                                    <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                    </div>
                    <div data-region="header-placeholder">
                        <div class="d-flex">
                            <div
                                class="ml-2 rounded-circle bg-pulse-grey align-self-center"
                                style="height: 38px; width: 38px"
                            >
                            </div>
                            <div class="ml-2 " style="flex: 1">
                                <div
                                    class="mt-1 bg-pulse-grey w-75"
                                    style="height: 16px;"
                                >
                                </div>
                            </div>
                            <div
                                class="ml-2 bg-pulse-grey align-self-center"
                                style="height: 16px; width: 20px"
                            >
                            </div>
                        </div>
                    </div>
                    <div
                        class="hidden position-absolute z-index-1"
                        data-region="confirm-dialogue-container"
                        style="top: 0; bottom: -1px; right: 0; left: 0; background: rgba(0,0,0,0.3);"
                    ></div>
                </div>                <div class="border-bottom p-1 px-sm-2" aria-hidden="false"  data-region="view-overview">
                    <div class="d-flex align-items-center">
                        <div class="input-group simplesearchform">
                            <input
                                type="text"
                                class="form-control"
                                placeholder="Recherche"
                                aria-label="Recherche"
                                data-region="view-overview-search-input"
                            >
                            <div class="input-group-append">
                                <span class="icon-no-margin btn btn-submit">
                                    <i class="icon fa fa-search fa-fw " aria-hidden="true"  ></i>
                                </span>
                            </div>
                        </div>
                        <div class="ml-2">
                            <a
                                href="#"
                                data-route="view-settings"
                                data-route-param="15830"
                                aria-label="Réglages"
                                role="button"
                            >
                                <i class="icon fa fa-cog fa-fw " aria-hidden="true"  ></i>
                            </a>
                        </div>
                    </div>
                    <div class="text-right mt-sm-3">
                        <a href="#" data-route="view-contacts" role="button">
                            <i class="icon fa fa-user fa-fw " aria-hidden="true"  ></i>
                            Contacts
                            <span
                                class="badge badge-primary bg-primary ml-2 hidden"
                                data-region="contact-request-count"
                            >
                                <span aria-hidden="true">0</span>
                                <span class="sr-only">Il y a 0 demandes de contact en attente</span>
                            </span>
                        </a>
                    </div>
                </div>
                
                <div class="hidden border-bottom p-1 px-sm-2 view-search"  aria-hidden="true" data-region="view-search">
                    <div class="d-flex align-items-center">
                        <a
                            class="mr-2 align-self-stretch d-flex align-items-center"
                            href="#"
                            data-route-back
                            data-action="cancel-search"
                            role="button"
                        >
                            <div class="icon-back-in-drawer">
                                <span class="dir-rtl-hide"><i class="icon fa fa-chevron-left fa-fw " aria-hidden="true"  ></i></span>
                                <span class="dir-ltr-hide"><i class="icon fa fa-chevron-right fa-fw " aria-hidden="true"  ></i></span>
                            </div>
                            <div class="icon-back-in-app">
                                <span class="dir-rtl-hide"><i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i></span>
                            </div>                        </a>
                        <div class="input-group simplesearchform">
                            <input
                                type="text"
                                class="form-control"
                                placeholder="Recherche"
                                aria-label="Recherche"
                                data-region="search-input"
                            >
                            <div class="input-group-append">
                                <button
                                    class="btn btn-submit icon-no-margin"
                                    type="button"
                                    data-action="search"
                                    aria-label="Recherche"
                                >
                                    <span data-region="search-icon-container">
                                        <i class="icon fa fa-search fa-fw " aria-hidden="true"  ></i>
                                    </span>
                                    <span class="hidden" data-region="loading-icon-container">
                                        <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
                                    </span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>                
                <div class="hidden border-bottom p-1 px-sm-2 pb-sm-3" aria-hidden="true" data-region="view-settings">
                    <div class="d-flex align-items-center">
                        <div class="align-self-stretch" >
                            <a class="h-100 d-flex mr-2 align-items-center" href="#" data-route-back role="button">
                                <div class="icon-back-in-drawer">
                                    <span class="dir-rtl-hide"><i class="icon fa fa-chevron-left fa-fw " aria-hidden="true"  ></i></span>
                                    <span class="dir-ltr-hide"><i class="icon fa fa-chevron-right fa-fw " aria-hidden="true"  ></i></span>
                                </div>
                                <div class="icon-back-in-app">
                                    <span class="dir-rtl-hide"><i class="icon fa fa-times fa-fw " aria-hidden="true"  ></i></span>
                                </div>                            </a>
                        </div>
                        <div>
                            Paramètres
                        </div>
                    </div>
                </div>
            </div>
            <div class="body-container position-relative" data-region="body-container">
                
                <div
                    class="hidden"
                    data-region="view-contact"
                    aria-hidden="true"
                >
                    <div class="p-2 pt-3" data-region="content-container"></div>
                </div>                <div class="hidden h-100" data-region="view-contacts" aria-hidden="true" data-user-id="15830">
                    <div class="d-flex flex-column h-100">
                        <div class="p-3 border-bottom">
                            <ul class="nav nav-pills nav-fill" role="tablist">
                                <li class="nav-item">
                                    <a
                                        id="contacts-tab-66179d5dc616366179d5dae8f59"
                                        class="nav-link active"
                                        href="#contacts-tab-panel-66179d5dc616366179d5dae8f59"
                                        data-toggle="tab"
                                        data-action="show-contacts-section"
                                        role="tab"
                                        aria-controls="contacts-tab-panel-66179d5dc616366179d5dae8f59"
                                        aria-selected="true"
                                    >
                                        Contacts
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a
                                        id="requests-tab-66179d5dc616366179d5dae8f59"
                                        class="nav-link"
                                        href="#requests-tab-panel-66179d5dc616366179d5dae8f59"
                                        data-toggle="tab"
                                        data-action="show-requests-section"
                                        role="tab"
                                        aria-controls="requests-tab-panel-66179d5dc616366179d5dae8f59"
                                        aria-selected="false"
                                    >
                                        Demandes
                                        <span class="badge badge-primary bg-primary ml-2 hidden"
                                            data-region="contact-request-count"
                                        >
                                            <span aria-hidden="true">0</span>
                                            <span class="sr-only">Il y a 0 demandes de contact en attente</span>
                                        </span>
                                    </a>
                                </li>
                            </ul>
                        </div>
                        <div class="tab-content d-flex flex-column h-100">
                                            <div
                    class="tab-pane fade show active h-100 lazy-load-list"
                    aria-live="polite"
                    data-region="lazy-load-list"
                    data-user-id="15830"
                                        id="contacts-tab-panel-66179d5dc616366179d5dae8f59"
                    data-section="contacts"
                    role="tabpanel"
                    aria-labelledby="contacts-tab-66179d5dc616366179d5dae8f59"

                >
                    
                    <div class="hidden text-center p-2" data-region="empty-message-container">
                        Aucun contact
                    </div>
                    <div class="hidden list-group" data-region="content-container">
                        
                    </div>
                    <div class="list-group" data-region="placeholder-container">
                        
                    </div>
                    <div class="w-100 text-center p-3 hidden" data-region="loading-icon-container" >
                        <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
                    </div>
                </div>
                
                                            <div
                    class="tab-pane fade h-100 lazy-load-list"
                    aria-live="polite"
                    data-region="lazy-load-list"
                    data-user-id="15830"
                                        id="requests-tab-panel-66179d5dc616366179d5dae8f59"
                    data-section="requests"
                    role="tabpanel"
                    aria-labelledby="requests-tab-66179d5dc616366179d5dae8f59"

                >
                    
                    <div class="hidden text-center p-2" data-region="empty-message-container">
                        Aucune demande de contact
                    </div>
                    <div class="hidden list-group" data-region="content-container">
                        
                    </div>
                    <div class="list-group" data-region="placeholder-container">
                        
                    </div>
                    <div class="w-100 text-center p-3 hidden" data-region="loading-icon-container" >
                        <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
                    </div>
                </div>
                        </div>
                    </div>
                </div>
                
                <div
                    class="view-conversation hidden h-100"
                    aria-hidden="true"
                    data-region="view-conversation"
                    data-user-id="15830"
                    data-midnight="1712786400"
                    data-message-poll-min="10"
                    data-message-poll-max="120"
                    data-message-poll-after-max="300"
                    style="overflow-y: auto; overflow-x: hidden"
                >
                    <div class="position-relative h-100" data-region="content-container" style="overflow-y: auto; overflow-x: hidden">
                        <div class="content-message-container hidden h-100 px-2 pt-0" data-region="content-message-container" role="log" style="overflow-y: auto; overflow-x: hidden">
                            <div class="py-3 sticky-top z-index-1 border-bottom text-center hidden" data-region="contact-request-sent-message-container">
                                <p class="m-0">Demande de contact envoyée</p>
                                <p class="font-italic font-weight-light" data-region="text"></p>
                            </div>
                            <div class="p-3 text-center hidden" data-region="self-conversation-message-container">
                                <p class="m-0">Espace personnel</p>
                                <p class="font-italic font-weight-light" data-region="text">Enregistrer des brouillons, liens, note, etc. pour un usage ultérieur.</p>
                           </div>
                            <div class="hidden text-center p-3" data-region="more-messages-loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</div>
                        </div>
                        <div class="p-4 w-100 h-100 hidden position-absolute z-index-1" data-region="confirm-dialogue-container" style="top: 0; background: rgba(0,0,0,0.3);">
                            
                            <div class="p-3 bg-white" data-region="confirm-dialogue" role="alert">
                                <p class="text-muted" data-region="dialogue-text"></p>
                                <div class="mb-2 custom-control custom-checkbox hidden" data-region="delete-messages-for-all-users-toggle-container">
                                    <input type="checkbox" class="custom-control-input" id="delete-messages-for-all-users" data-region="delete-messages-for-all-users-toggle">
                                    <label class="custom-control-label text-muted" for="delete-messages-for-all-users">
                                        Supprimer pour moi et et pour tous les autres
                                    </label>
                                </div>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-block">
                                    <span data-region="dialogue-button-text">Bloc</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-unblock">
                                    <span data-region="dialogue-button-text">Débloquer</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-remove-contact">
                                    <span data-region="dialogue-button-text">Supprimer</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-add-contact">
                                    <span data-region="dialogue-button-text">Ajouter</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-delete-selected-messages">
                                    <span data-region="dialogue-button-text">Supprimer</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="confirm-delete-conversation">
                                    <span data-region="dialogue-button-text">Supprimer</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="request-add-contact">
                                    <span data-region="dialogue-button-text">Envoyer une demande de contact</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block hidden" data-action="accept-contact-request">
                                    <span data-region="dialogue-button-text">Accepter et ajouter aux contacts</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-secondary btn-block hidden" data-action="decline-contact-request">
                                    <span data-region="dialogue-button-text">Décliner</span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                </button>
                                <button type="button" class="btn btn-primary btn-block" data-action="okay-confirm">OK</button>
                                <button type="button" class="btn btn-secondary btn-block" data-action="cancel-confirm">Annuler</button>
                            </div>
                        </div>
                        <div class="px-2 pb-2 pt-0" data-region="content-placeholder">
                            <div class="h-100 d-flex flex-column">
                                <div
                                    class="px-2 pb-2 pt-0 bg-light h-100"
                                    style="overflow-y: auto"
                                >
                                    <div class="mt-4">
                                        <div class="mb-4">
                                            <div class="mx-auto bg-white" style="height: 25px; width: 100px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                    </div>                                    <div class="mt-4">
                                        <div class="mb-4">
                                            <div class="mx-auto bg-white" style="height: 25px; width: 100px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                    </div>                                    <div class="mt-4">
                                        <div class="mb-4">
                                            <div class="mx-auto bg-white" style="height: 25px; width: 100px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                    </div>                                    <div class="mt-4">
                                        <div class="mb-4">
                                            <div class="mx-auto bg-white" style="height: 25px; width: 100px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                    </div>                                    <div class="mt-4">
                                        <div class="mb-4">
                                            <div class="mx-auto bg-white" style="height: 25px; width: 100px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                        <div class="d-flex flex-column p-2 bg-white rounded mb-2">
                                            <div class="d-flex align-items-center mb-2">
                                                <div class="mr-2">
                                                    <div class="rounded-circle bg-pulse-grey" style="height: 35px; width: 35px"></div>
                                                </div>
                                                <div class="mr-4 w-75 bg-pulse-grey" style="height: 16px"></div>
                                                <div class="ml-auto bg-pulse-grey" style="width: 35px; height: 16px"></div>
                                            </div>
                                            <div class="bg-pulse-grey w-100" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-100 mt-2" style="height: 16px"></div>
                                            <div class="bg-pulse-grey w-75 mt-2" style="height: 16px"></div>
                                        </div>
                                    </div>                                </div>
                            </div>                        </div>
                    </div>
                </div>
                
                <div
                    class="hidden"
                    aria-hidden="true"
                    data-region="view-group-info"
                >
                    <div
                        class="pt-3 h-100 d-flex flex-column"
                        data-region="group-info-content-container"
                        style="overflow-y: auto"
                    ></div>
                </div>                <div class="h-100 view-overview-body" aria-hidden="false" data-region="view-overview"  data-user-id="15830">
                    <div id="message-drawer-view-overview-container-66179d5dc616366179d5dae8f59" class="d-flex flex-column h-100" style="overflow-y: auto">
                            
                            
                            <div
                                class="section border-0 card rounded-0"
                                data-region="view-overview-favourites"
                            >
                                <div id="view-overview-favourites-toggle" class="card-header rounded-0" data-region="toggle">
                                    <button
                                        class="btn btn-link w-100 text-left p-1 p-sm-2 d-flex rounded-0 align-items-center overview-section-toggle collapsed"
                                        data-toggle="collapse"
                                        data-target="#view-overview-favourites-target-66179d5dc616366179d5dae8f59"
                                        aria-expanded="false"
                                        aria-controls="view-overview-favourites-target-66179d5dc616366179d5dae8f59"
                                    >
                                        <span class="collapsed-icon-container">
                                            <i class="icon fa fa-caret-right fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="expanded-icon-container">
                                            <i class="icon fa fa-caret-down fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="font-weight-bold">Favoris</span>
                                        <small class="hidden ml-1" data-region="section-total-count-container">
                                            (<span aria-hidden="true" data-region="section-total-count"></span><span class="sr-only"> conversations</span>)
                                        </small>
                                        <span class="hidden ml-2" data-region="loading-icon-container">
                                            <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
                                        </span>
                                        <span
                                            class="hidden badge badge-pill badge-primary ml-auto bg-primary"
                                            data-region="section-unread-count"
                                        >
                                            <span aria-hidden="true"></span>
                                            <span class="sr-only">Il y a  conversations non lues</span>
                                        </span>
                                    </button>
                                </div>
                                                            <div
                                class="collapse border-bottom  lazy-load-list"
                                aria-live="polite"
                                data-region="lazy-load-list"
                                data-user-id="15830"
                                            id="view-overview-favourites-target-66179d5dc616366179d5dae8f59"
            aria-labelledby="view-overview-favourites-toggle"
            data-parent="#message-drawer-view-overview-container-66179d5dc616366179d5dae8f59"

                            >
                                
                                <div class="hidden text-center p-2" data-region="empty-message-container">
                                            <p class="text-muted mt-2">Aucune conversation favorite</p>

                                </div>
                                <div class="hidden list-group" data-region="content-container">
                                    
                                </div>
                                <div class="list-group" data-region="placeholder-container">
                                            <div class="text-center py-2"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</div>

                                </div>
                                <div class="w-100 text-center p-3 hidden" data-region="loading-icon-container" >
                                    <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
                                </div>
                            </div>
                            </div>
                            
                            
                            <div
                                class="section border-0 card rounded-0"
                                data-region="view-overview-group-messages"
                            >
                                <div id="view-overview-group-messages-toggle" class="card-header rounded-0" data-region="toggle">
                                    <button
                                        class="btn btn-link w-100 text-left p-1 p-sm-2 d-flex rounded-0 align-items-center overview-section-toggle collapsed"
                                        data-toggle="collapse"
                                        data-target="#view-overview-group-messages-target-66179d5dc616366179d5dae8f59"
                                        aria-expanded="false"
                                        aria-controls="view-overview-group-messages-target-66179d5dc616366179d5dae8f59"
                                    >
                                        <span class="collapsed-icon-container">
                                            <i class="icon fa fa-caret-right fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="expanded-icon-container">
                                            <i class="icon fa fa-caret-down fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="font-weight-bold">Groupe</span>
                                        <small class="hidden ml-1" data-region="section-total-count-container">
                                            (<span aria-hidden="true" data-region="section-total-count"></span><span class="sr-only"> conversations</span>)
                                        </small>
                                        <span class="hidden ml-2" data-region="loading-icon-container">
                                            <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
                                        </span>
                                        <span
                                            class="hidden badge badge-pill badge-primary ml-auto bg-primary"
                                            data-region="section-unread-count"
                                        >
                                            <span aria-hidden="true"></span>
                                            <span class="sr-only">Il y a  conversations non lues</span>
                                        </span>
                                    </button>
                                </div>
                                                            <div
                                class="collapse border-bottom  lazy-load-list"
                                aria-live="polite"
                                data-region="lazy-load-list"
                                data-user-id="15830"
                                            id="view-overview-group-messages-target-66179d5dc616366179d5dae8f59"
            aria-labelledby="view-overview-group-messages-toggle"
            data-parent="#message-drawer-view-overview-container-66179d5dc616366179d5dae8f59"

                            >
                                
                                <div class="hidden text-center p-2" data-region="empty-message-container">
                                            <p class="text-muted mt-2">Pas de conversation de groupe</p>

                                </div>
                                <div class="hidden list-group" data-region="content-container">
                                    
                                </div>
                                <div class="list-group" data-region="placeholder-container">
                                            <div class="text-center py-2"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</div>

                                </div>
                                <div class="w-100 text-center p-3 hidden" data-region="loading-icon-container" >
                                    <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
                                </div>
                            </div>
                            </div>
                            
                            
                            <div
                                class="section border-0 card rounded-0"
                                data-region="view-overview-messages"
                            >
                                <div id="view-overview-messages-toggle" class="card-header rounded-0" data-region="toggle">
                                    <button
                                        class="btn btn-link w-100 text-left p-1 p-sm-2 d-flex rounded-0 align-items-center overview-section-toggle collapsed"
                                        data-toggle="collapse"
                                        data-target="#view-overview-messages-target-66179d5dc616366179d5dae8f59"
                                        aria-expanded="false"
                                        aria-controls="view-overview-messages-target-66179d5dc616366179d5dae8f59"
                                    >
                                        <span class="collapsed-icon-container">
                                            <i class="icon fa fa-caret-right fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="expanded-icon-container">
                                            <i class="icon fa fa-caret-down fa-fw " aria-hidden="true"  ></i>
                                        </span>
                                        <span class="font-weight-bold">Privée</span>
                                        <small class="hidden ml-1" data-region="section-total-count-container">
                                            (<span aria-hidden="true" data-region="section-total-count"></span><span class="sr-only"> conversations</span>)
                                        </small>
                                        <span class="hidden ml-2" data-region="loading-icon-container">
                                            <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
                                        </span>
                                        <span
                                            class="hidden badge badge-pill badge-primary ml-auto bg-primary"
                                            data-region="section-unread-count"
                                        >
                                            <span aria-hidden="true"></span>
                                            <span class="sr-only">Il y a  conversations non lues</span>
                                        </span>
                                    </button>
                                </div>
                                                            <div
                                class="collapse border-bottom  lazy-load-list"
                                aria-live="polite"
                                data-region="lazy-load-list"
                                data-user-id="15830"
                                            id="view-overview-messages-target-66179d5dc616366179d5dae8f59"
            aria-labelledby="view-overview-messages-toggle"
            data-parent="#message-drawer-view-overview-container-66179d5dc616366179d5dae8f59"

                            >
                                
                                <div class="hidden text-center p-2" data-region="empty-message-container">
                                            <p class="text-muted mt-2">Pas de conversation privée</p>

                                </div>
                                <div class="hidden list-group" data-region="content-container">
                                    
                                </div>
                                <div class="list-group" data-region="placeholder-container">
                                            <div class="text-center py-2"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</div>

                                </div>
                                <div class="w-100 text-center p-3 hidden" data-region="loading-icon-container" >
                                    <span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
                                </div>
                            </div>
                            </div>
                    </div>
                </div>
                
                <div
                    data-region="view-search"
                    aria-hidden="true"
                    class="h-100 hidden"
                    data-user-id="15830"
                    data-users-offset="0"
                    data-messages-offset="0"
                    style="overflow-y: auto"
                    
                >
                    <div class="hidden" data-region="search-results-container" style="overflow-y: auto">
                        
                        <div class="d-flex flex-column">
                            <div class="mb-3 bg-white" data-region="all-contacts-container">
                                <div data-region="contacts-container"  class="pt-2">
                                    <h4 class="h6 px-2">Contacts</h4>
                                    <div class="list-group" data-region="list"></div>
                                </div>
                                <div data-region="non-contacts-container" class="pt-2 border-top">
                                    <h4 class="h6 px-2">Non contact</h4>
                                    <div class="list-group" data-region="list"></div>
                                </div>
                                <div class="text-right">
                                    <button class="btn btn-link text-primary" data-action="load-more-users">
                                        <span data-region="button-text">Charger plus</span>
                                        <span data-region="loading-icon-container" class="hidden"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                    </button>
                                </div>
                            </div>
                            <div class="bg-white" data-region="messages-container">
                                <h4 class="h6 px-2 pt-2">Messages personnels</h4>
                                <div class="list-group" data-region="list"></div>
                                <div class="text-right">
                                    <button class="btn btn-link text-primary" data-action="load-more-messages">
                                        <span data-region="button-text">Charger plus</span>
                                        <span data-region="loading-icon-container" class="hidden"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                    </button>
                                </div>
                            </div>
                            <p class="hidden p-3 text-center" data-region="no-results-container">Aucun résultat</p>
                        </div>                    </div>
                    <div class="hidden" data-region="loading-placeholder">
                        <div class="text-center pt-3 icon-size-4"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</div>
                    </div>
                    <div class="p-3 text-center" data-region="empty-message-container">
                        <p>Rechercher des personnes et des messages</p>
                    </div>
                </div>                
                <div class="h-100 hidden bg-white" aria-hidden="true" data-region="view-settings">
                    <div class="hidden" data-region="content-container">
                        
                        <div data-region="settings" class="p-3">
                            <h3 class="h6 font-weight-bold">Confidentialité</h3>
                            <p>Vous pouvez choisir qui peut vous envoyer un message personnel</p>
                            <div data-preference="blocknoncontacts" class="mb-3">
                                <fieldset>
                                    <legend class="sr-only">Accepter des messages de :</legend>
                                        <div class="custom-control custom-radio mb-2">
                                            <input
                                                type="radio"
                                                name="message_blocknoncontacts"
                                                class="custom-control-input"
                                                id="block-noncontacts-66179d5dc616366179d5dae8f59-1"
                                                value="1"
                                            >
                                            <label class="custom-control-label ml-2" for="block-noncontacts-66179d5dc616366179d5dae8f59-1">
                                                Mes contacts seulement
                                            </label>
                                        </div>
                                        <div class="custom-control custom-radio mb-2">
                                            <input
                                                type="radio"
                                                name="message_blocknoncontacts"
                                                class="custom-control-input"
                                                id="block-noncontacts-66179d5dc616366179d5dae8f59-0"
                                                value="0"
                                            >
                                            <label class="custom-control-label ml-2" for="block-noncontacts-66179d5dc616366179d5dae8f59-0">
                                                Mes contacts et tout le monde dans mes cours
                                            </label>
                                        </div>
                                        <div class="custom-control custom-radio mb-2">
                                            <input
                                                type="radio"
                                                name="message_blocknoncontacts"
                                                class="custom-control-input"
                                                id="block-noncontacts-66179d5dc616366179d5dae8f59-2"
                                                value="2"
                                            >
                                            <label class="custom-control-label ml-2" for="block-noncontacts-66179d5dc616366179d5dae8f59-2">
                                                Tout le monde sur le site
                                            </label>
                                        </div>
                                </fieldset>
                            </div>
                        
                            <div class="hidden" data-region="notification-preference-container">
                                <h3 class="mb-2 mt-4 h6 font-weight-bold">Préférences de notification</h3>
                            </div>
                        
                            <h3 class="mb-2 mt-4 h6 font-weight-bold">Général</h3>
                            <div data-preference="entertosend">
                                <div class="custom-control custom-switch">
                                    <input type="checkbox" class="custom-control-input" id="enter-to-send-66179d5dc616366179d5dae8f59" checked>
                                    <label class="custom-control-label" for="enter-to-send-66179d5dc616366179d5dae8f59">
                                        Taper entrée pour envoyer
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div data-region="placeholder-container">
                        
                        <div class="d-flex flex-column p-3">
                            <div class="w-25 bg-pulse-grey h6" style="height: 18px"></div>
                            <div class="w-75 bg-pulse-grey mb-4" style="height: 18px"></div>
                            <div class="mb-3">
                                <div class="w-100 d-flex mb-3">
                                    <div class="bg-pulse-grey rounded-circle" style="width: 18px; height: 18px"></div>
                                    <div class="bg-pulse-grey w-50 ml-2" style="height: 18px"></div>
                                </div>
                                <div class="w-100 d-flex mb-3">
                                    <div class="bg-pulse-grey rounded-circle" style="width: 18px; height: 18px"></div>
                                    <div class="bg-pulse-grey w-50 ml-2" style="height: 18px"></div>
                                </div>
                                <div class="w-100 d-flex mb-3">
                                    <div class="bg-pulse-grey rounded-circle" style="width: 18px; height: 18px"></div>
                                    <div class="bg-pulse-grey w-50 ml-2" style="height: 18px"></div>
                                </div>
                            </div>
                            <div class="w-50 bg-pulse-grey h6 mb-3 mt-2" style="height: 18px"></div>
                            <div class="mb-4">
                                <div class="w-100 d-flex mb-2 align-items-center">
                                    <div class="bg-pulse-grey w-25" style="width: 18px; height: 27px"></div>
                                    <div class="bg-pulse-grey w-25 ml-2" style="height: 18px"></div>
                                </div>
                                <div class="w-100 d-flex mb-2 align-items-center">
                                    <div class="bg-pulse-grey w-25" style="width: 18px; height: 27px"></div>
                                    <div class="bg-pulse-grey w-25 ml-2" style="height: 18px"></div>
                                </div>
                            </div>
                            <div class="w-25 bg-pulse-grey h6 mb-3 mt-2" style="height: 18px"></div>
                            <div class="mb-3">
                                <div class="w-100 d-flex mb-2 align-items-center">
                                    <div class="bg-pulse-grey w-25" style="width: 18px; height: 27px"></div>
                                    <div class="bg-pulse-grey w-50 ml-2" style="height: 18px"></div>
                                </div>
                            </div>
                        </div>                    </div>
                </div>            </div>
            <div class="footer-container position-relative" data-region="footer-container">
                
                <div
                    class="hidden border-top bg-white position-relative"
                    aria-hidden="true"
                    data-region="view-conversation"
                    data-enter-to-send="1"
                >
                    <div class="hidden p-sm-2" data-region="content-messages-footer-container">
                        
                            <div
                                class="emoji-auto-complete-container w-100 hidden"
                                data-region="emoji-auto-complete-container"
                                aria-live="polite"
                                aria-hidden="true"
                            >
                            </div>
                        <div class="d-flex mt-sm-1">
                            <textarea
                                dir="auto"
                                data-region="send-message-txt"
                                class="form-control bg-light"
                                rows="3"
                                data-auto-rows
                                data-min-rows="3"
                                data-max-rows="5"
                                aria-label="Écrire un message"
                                placeholder="Écrire un message"
                                style="resize: none"
                                maxlength="4096"
                            ></textarea>
                        
                            <div class="position-relative d-flex flex-column">
                                    <div
                                        data-region="emoji-picker-container"
                                        class="emoji-picker-container hidden"
                                        aria-hidden="true"
                                    >
                                        
                                        <div
                                            data-region="emoji-picker"
                                            class="card shadow emoji-picker"
                                        >
                                            <div class="card-header px-1 pt-1 pb-0 d-flex justify-content-between flex-shrink-0">
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0 selected"
                                                    data-action="show-category"
                                                    data-category="Recent"
                                                    title="Récents"
                                                >
                                                    <i class="icon fa fa-clock-o fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Smileys & Emotion"
                                                    title="Smileys et émotion"
                                                >
                                                    <i class="icon fa fa-smile-o fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="People & Body"
                                                    title="Personnes et corps"
                                                >
                                                    <i class="icon fa fa-male fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Animals & Nature"
                                                    title="Animaux & nature"
                                                >
                                                    <i class="icon fa fa-leaf fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Food & Drink"
                                                    title="Nourriture & boissons"
                                                >
                                                    <i class="icon fa fa-cutlery fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Travel & Places"
                                                    title="Voyages & lieux"
                                                >
                                                    <i class="icon fa fa-plane fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Activities"
                                                    title="Activités"
                                                >
                                                    <i class="icon fa fa-futbol-o fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Objects"
                                                    title="Objets"
                                                >
                                                    <i class="icon fa fa-lightbulb-o fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Symbols"
                                                    title="Symboles"
                                                >
                                                    <i class="icon fa fa-heart fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                                <button
                                                    class="btn btn-outline-secondary icon-no-margin category-button rounded-0"
                                                    data-action="show-category"
                                                    data-category="Flags"
                                                    title="Drapeaux"
                                                >
                                                    <i class="icon fa fa-flag fa-fw " aria-hidden="true"  ></i>
                                                </button>
                                            </div>
                                            <div class="card-body p-2 d-flex flex-column overflow-hidden">
                                                <div class="input-group mb-1 flex-shrink-0">
                                                    <div class="input-group-prepend">
                                                        <span class="input-group-text pr-0 bg-white text-muted">
                                                            <i class="icon fa fa-search fa-fw " aria-hidden="true"  ></i>
                                                        </span>
                                                    </div>
                                                    <input
                                                        type="text"
                                                        class="form-control border-left-0"
                                                        placeholder="Rechercher"
                                                        aria-label="Rechercher"
                                                        data-region="search-input"
                                                    >
                                                </div>
                                                <div class="flex-grow-1 overflow-auto emojis-container h-100" data-region="emojis-container">
                                                    <div class="position-relative" data-region="row-container"></div>
                                                </div>
                                                <div class="flex-grow-1 overflow-auto search-results-container h-100 hidden" data-region="search-results-container">
                                                    <div class="position-relative" data-region="row-container"></div>
                                                </div>
                                            </div>
                                            <div
                                                class="card-footer d-flex flex-shrink-0"
                                                data-region="footer"
                                            >
                                                <div class="emoji-preview" data-region="emoji-preview"></div>
                                                <div data-region="emoji-short-name" class="emoji-short-name text-muted text-wrap ml-2"></div>
                                            </div>
                                        </div>
                                    </div>
                                    <button
                                        class="btn btn-link btn-icon icon-size-3 ml-1"
                                        aria-label="Activer/désactiver le sélecteur d'émojis"
                                        data-action="toggle-emoji-picker"
                                    >
                                        <i class="icon fa fa-smile-o fa-fw " aria-hidden="true"  ></i>
                                    </button>
                                <button
                                    class="btn btn-link btn-icon icon-size-3 ml-1 mt-auto"
                                    aria-label="Envoyer message personnel"
                                    data-action="send-message"
                                >
                                    <span data-region="send-icon-container"><i class="icon fa fa-paper-plane fa-fw " aria-hidden="true"  ></i></span>
                                    <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div class="hidden p-sm-2" data-region="content-messages-footer-edit-mode-container">
                        
                        <div class="d-flex p-3 justify-content-end">
                            <button
                                class="btn btn-link btn-icon my-1 icon-size-4"
                                data-action="delete-selected-messages"
                                data-toggle="tooltip"
                                data-placement="top"
                                title="Supprimer les messages sélectionnés"
                            >
                                <span data-region="icon-container"><i class="icon fa fa-trash fa-fw " aria-hidden="true"  ></i></span>
                                <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                                <span class="sr-only">Supprimer les messages sélectionnés</span>
                            </button>
                        </div>                    </div>
                    <div class="hidden bg-secondary p-sm-3" data-region="content-messages-footer-require-contact-container">
                        
                        <div class="p-3 bg-white">
                            <p data-region="title"></p>
                            <p class="text-muted" data-region="text"></p>
                            <button type="button" class="btn btn-primary btn-block" data-action="request-add-contact">
                                <span data-region="dialogue-button-text">Envoyer une demande de contact</span>
                                <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                            </button>
                        </div>
                    </div>
                    <div class="hidden bg-secondary p-sm-3" data-region="content-messages-footer-require-unblock-container">
                        
                        <div class="p-3 bg-white">
                            <p class="text-muted" data-region="text">Vous avez bloqué cet utilisateur.</p>
                            <button type="button" class="btn btn-primary btn-block" data-action="request-unblock">
                                <span data-region="dialogue-button-text">Débloquer l'utilisateur</span>
                                <span class="hidden" data-region="loading-icon-container"><span class="loading-icon icon-no-margin"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Chargement" role="img" aria-label="Chargement"></i></span>
</span>
                            </button>
                        </div>
                    </div>
                    <div class="hidden bg-secondary p-sm-3" data-region="content-messages-footer-unable-to-message">
                        
                        <div class="p-3 bg-white">
                            <p class="text-muted" data-region="text">Vous ne pouvez pas envoyer un message à cet utilisateur</p>
                        </div>
                    </div>
                    <div class="p-sm-2" data-region="placeholder-container">
                        <div class="d-flex">
                            <div class="bg-pulse-grey w-100" style="height: 80px"></div>
                            <div class="mx-2 mb-2 align-self-end bg-pulse-grey" style="height: 20px; width: 20px"></div>
                        </div>                    </div>
                    <div
                        class="hidden position-absolute z-index-1"
                        data-region="confirm-dialogue-container"
                        style="top: -1px; bottom: 0; right: 0; left: 0; background: rgba(0,0,0,0.3);"
                    ></div>
                </div>                    <div data-region="view-overview" class="text-center">
                        <a href="https://moodle.u-bordeaux.fr/message/index.php">
                            Tout afficher
                        </a>
                    </div>
            </div>
        </div>

</div>
</div>

</body>
</html>