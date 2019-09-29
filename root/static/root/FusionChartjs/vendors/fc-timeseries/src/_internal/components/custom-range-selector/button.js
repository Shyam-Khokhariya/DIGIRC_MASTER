import{SmartRenderer}from'../../../../../fc-core/src/component-interface';class Button extends SmartRenderer{constructor(a){super(a);let b=this,c=b.config;c.clickHandler=function(){b.getLinkedParent().submitData(c.type)},c.mouseoverHandler=function(){b.setData({buttonStyle:c['button:hover']},!0)},c.mouseoutHandler=function(){b.config&&b.setData({buttonStyle:c['button:hoverout']},!0)}}__setDefaultConfig(){let a=this.config;a.height=10,a.width=20,a.label='Apply',a._buttonStyle={"-webkit-border-radius":'2px',backgroundColor:'#5648D4',border:'1px solid #5648D4',borderRadius:'2px',color:'#60634E',cursor:'pointer',paddingTop:'1px',textAlign:'center',zIndex:21,display:'flex',width:66,height:22,"line-height":'9px',"justify-content":'center',"align-items":'center',"font-size":'11px'},a.clickHandler=function(){this.getLinkedParent().submitData()}}configureAttributes(a={}){super.configureAttributes(a);let b=this,c=b.config,d=b.getFromEnv('getStyleDef'),e=b.getFromEnv('baseTextStyle');Object.keys(a).forEach(b=>c[b]=a[b]),c._finalStyle=Object.assign({},c._buttonStyle,e,d(c.customStyle),d(c.buttonStyle))}getDimension(){var a=Math.max;let b=this,c=b.config,d=c._finalStyle['font-size'],e=b.getFromEnv('fontParser');return c.width=a(+c._finalStyle.width||0,6*e(d)),c.height=a(+c._finalStyle.height||0,2*e(d)),{width:c.width,height:c.height}}setTranslation(a,b){this.config.position={x:a,y:b}}draw(){let a=this,b=a.config,c=b.position;a.addGraphicalElement({el:'html',attr:{text:b.label,type:'div',width:b.width,height:b.height,x:c.x,y:c.y},component:a,container:{id:'box-container',label:'box-container',isParent:!0},css:b._finalStyle,label:'button',id:'button'}),this.addEventWithWrapper()}addEventWithWrapper(){let a=this,b=a.getFromEnv('eventWrapper'),c=a.getGraphicalElement('button','button'),{clickHandler:d,mouseoverHandler:e,mouseoutHandler:f}=a.config;b.on(c.element,'fc-click',d),b.on(c.element,'fc-mouseover',e),b.on(c.element,'fc-mouseout',f)}removeEventWithWrapper(){let a=this,b=a.getFromEnv('eventWrapper'),c=a.getGraphicalElement('button','button'),{clickHandler:d,mouseoverHandler:e,mouseoutHandler:f}=a.config;b.off(c.element,'fc-click',d),b.off(c.element,'fc-mouseover',e),b.off(c.element,'fc-mouseout',f)}remove(a){this.removeEventWithWrapper(),super.remove(a)}}export default Button;