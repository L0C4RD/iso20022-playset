from . import base_types
from ._MaintenanceIdentificationAssociation1 import MaintenanceIdentificationAssociation1
from ._TrueFalseIndicator import TrueFalseIndicator
from ._AcceptorConfigurationDataSet6 import AcceptorConfigurationDataSet6
from ._DataSetCategory19Code import DataSetCategory19Code
from ._KEKIdentifier5 import KEKIdentifier5
from ._MaintenanceDelegateAction10 import MaintenanceDelegateAction10
from ._TerminalManagementAction3Code import TerminalManagementAction3Code
from ._Max35Text import Max35Text
from ._Max10KBinary import Max10KBinary
from ._Max3000Binary import Max3000Binary

class MaintenanceDelegation19(base_types._BaseFieldType):

	__slots__ = ["_DlgtdActn", "_POIIdAssoctn", "_ParamDataSet", "_MntncSvc", "_DlgtnTp", "_Cert", "_DlgtnScpId", "_DlgtnScpDef", "_PrtlDlgtn", "_POISubset", "_SmmtrcKey"]
	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if type(value) != base_types.auto else self.make_default("Cert")

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = None

	@property
	def DlgtdActn(self):
		return self._DlgtdActn

	@DlgtdActn.setter
	def DlgtdActn(self, value):
		self._DlgtdActn = value if type(value) != base_types.auto else self.make_default("DlgtdActn")

	@DlgtdActn.deleter
	def DlgtdActn(self):
		del self._DlgtdActn
		self._DlgtdActn = None

	@property
	def DlgtnScpDef(self):
		return self._DlgtnScpDef

	@DlgtnScpDef.setter
	def DlgtnScpDef(self, value):
		self._DlgtnScpDef = value if type(value) != base_types.auto else self.make_default("DlgtnScpDef")

	@DlgtnScpDef.deleter
	def DlgtnScpDef(self):
		del self._DlgtnScpDef
		self._DlgtnScpDef = None

	@property
	def DlgtnScpId(self):
		return self._DlgtnScpId

	@DlgtnScpId.setter
	def DlgtnScpId(self, value):
		self._DlgtnScpId = value if type(value) != base_types.auto else self.make_default("DlgtnScpId")

	@DlgtnScpId.deleter
	def DlgtnScpId(self):
		del self._DlgtnScpId
		self._DlgtnScpId = None

	@property
	def DlgtnTp(self):
		return self._DlgtnTp

	@DlgtnTp.setter
	def DlgtnTp(self, value):
		self._DlgtnTp = value if type(value) != base_types.auto else self.make_default("DlgtnTp")

	@DlgtnTp.deleter
	def DlgtnTp(self):
		del self._DlgtnTp
		self._DlgtnTp = None

	@property
	def MntncSvc(self):
		return self._MntncSvc

	@MntncSvc.setter
	def MntncSvc(self, value):
		self._MntncSvc = value if type(value) != base_types.auto else self.make_default("MntncSvc")

	@MntncSvc.deleter
	def MntncSvc(self):
		del self._MntncSvc
		self._MntncSvc = None

	@property
	def POIIdAssoctn(self):
		return self._POIIdAssoctn

	@POIIdAssoctn.setter
	def POIIdAssoctn(self, value):
		self._POIIdAssoctn = value if type(value) != base_types.auto else self.make_default("POIIdAssoctn")

	@POIIdAssoctn.deleter
	def POIIdAssoctn(self):
		del self._POIIdAssoctn
		self._POIIdAssoctn = None

	@property
	def POISubset(self):
		return self._POISubset

	@POISubset.setter
	def POISubset(self, value):
		self._POISubset = value if type(value) != base_types.auto else self.make_default("POISubset")

	@POISubset.deleter
	def POISubset(self):
		del self._POISubset
		self._POISubset = None

	@property
	def ParamDataSet(self):
		return self._ParamDataSet

	@ParamDataSet.setter
	def ParamDataSet(self, value):
		self._ParamDataSet = value if type(value) != base_types.auto else self.make_default("ParamDataSet")

	@ParamDataSet.deleter
	def ParamDataSet(self):
		del self._ParamDataSet
		self._ParamDataSet = None

	@property
	def PrtlDlgtn(self):
		return self._PrtlDlgtn

	@PrtlDlgtn.setter
	def PrtlDlgtn(self, value):
		self._PrtlDlgtn = value if type(value) != base_types.auto else self.make_default("PrtlDlgtn")

	@PrtlDlgtn.deleter
	def PrtlDlgtn(self):
		del self._PrtlDlgtn
		self._PrtlDlgtn = None

	@property
	def SmmtrcKey(self):
		return self._SmmtrcKey

	@SmmtrcKey.setter
	def SmmtrcKey(self, value):
		self._SmmtrcKey = value if type(value) != base_types.auto else self.make_default("SmmtrcKey")

	@SmmtrcKey.deleter
	def SmmtrcKey(self):
		del self._SmmtrcKey
		self._SmmtrcKey = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cert', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlgtdActn', type=MaintenanceDelegateAction10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnScpDef', type=Max3000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnScpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncSvc', type=DataSetCategory19Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIIdAssoctn', type=MaintenanceIdentificationAssociation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POISubset', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ParamDataSet', type=AcceptorConfigurationDataSet6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlDlgtn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SmmtrcKey', type=KEKIdentifier5, min=0, max=None, mutex_group=None, array=True),
	))

