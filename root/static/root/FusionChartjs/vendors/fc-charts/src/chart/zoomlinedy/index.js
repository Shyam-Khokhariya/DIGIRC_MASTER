import ZoomLine from'../zoomline';import{_feedAxesRawData,getSpecificxAxisConf,getSpecificyAxisConf,setAxisDimention}from'../_internal/msdybasecartesian';import axisFactory from'../../factories/cartesian-axis-dual-y';import datasetFactory from'../../factories/zoomline-dual-y-dataset';class ZoomLineDy extends ZoomLine{constructor(){super(),this.getSpecificxAxisConf=getSpecificxAxisConf,this.getSpecificyAxisConf=getSpecificyAxisConf,this.registerFactory('axis',axisFactory,['canvas']),this.registerFactory('dataset',datasetFactory,['vCanvas'])}static getName(){return'ZoomLineDy'}getName(){return'ZoomLineDy'}__setDefaultConfig(){super.__setDefaultConfig();let a=this.config;a.friendlyName='Zoomable and Panable Multi-series Dual-axis Line Chart',a.defaultDatasetType='zoomline',a.isdual=!0,a.syncaxislimits=0}_feedAxesRawData(){return _feedAxesRawData.call(this)}}ZoomLineDy.prototype.setAxisDimention=setAxisDimention;export default ZoomLineDy;