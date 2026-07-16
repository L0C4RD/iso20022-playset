# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorConfigurationDataSet7
from . import CryptographicKey19
from . import DataSetCategory19Code
from . import MaintenanceDelegateAction11
from . import MaintenanceIdentificationAssociation1
from . import Max10KBinary
from . import Max3000Binary
from . import Max35Text
from . import TerminalManagementAction3Code
from . import TrueFalseIndicator

class MaintenanceDelegation20(base_types._BaseFieldType):

	__slots__ = ["_Cert", "_DlgtdActn", "_DlgtnScpDef", "_DlgtnScpId", "_DlgtnTp", "_MntncSvc", "_POIIdAssoctn", "_POISubset", "_ParamDataSet", "_PrtlDlgtn", "_SmmtrcKey"]
	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if value is not None else base_types.UninitialisedField(self, 'Cert', Max10KBinary, True)

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = base_types.UninitialisedField(self, 'Cert', Max10KBinary, True)

	@property
	def DlgtdActn(self):
		return self._DlgtdActn

	@DlgtdActn.setter
	def DlgtdActn(self, value):
		self._DlgtdActn = value if value is not None else base_types.UninitialisedField(self, 'DlgtdActn', MaintenanceDelegateAction11, False)

	@DlgtdActn.deleter
	def DlgtdActn(self):
		del self._DlgtdActn
		self._DlgtdActn = base_types.UninitialisedField(self, 'DlgtdActn', MaintenanceDelegateAction11, False)

	@property
	def DlgtnScpDef(self):
		return self._DlgtnScpDef

	@DlgtnScpDef.setter
	def DlgtnScpDef(self, value):
		self._DlgtnScpDef = value if value is not None else base_types.UninitialisedField(self, 'DlgtnScpDef', Max3000Binary, False)

	@DlgtnScpDef.deleter
	def DlgtnScpDef(self):
		del self._DlgtnScpDef
		self._DlgtnScpDef = base_types.UninitialisedField(self, 'DlgtnScpDef', Max3000Binary, False)

	@property
	def DlgtnScpId(self):
		return self._DlgtnScpId

	@DlgtnScpId.setter
	def DlgtnScpId(self, value):
		self._DlgtnScpId = value if value is not None else base_types.UninitialisedField(self, 'DlgtnScpId', Max35Text, False)

	@DlgtnScpId.deleter
	def DlgtnScpId(self):
		del self._DlgtnScpId
		self._DlgtnScpId = base_types.UninitialisedField(self, 'DlgtnScpId', Max35Text, False)

	@property
	def DlgtnTp(self):
		return self._DlgtnTp

	@DlgtnTp.setter
	def DlgtnTp(self, value):
		self._DlgtnTp = value if value is not None else base_types.UninitialisedField(self, 'DlgtnTp', TerminalManagementAction3Code, False)

	@DlgtnTp.deleter
	def DlgtnTp(self):
		del self._DlgtnTp
		self._DlgtnTp = base_types.UninitialisedField(self, 'DlgtnTp', TerminalManagementAction3Code, False)

	@property
	def MntncSvc(self):
		return self._MntncSvc

	@MntncSvc.setter
	def MntncSvc(self, value):
		self._MntncSvc = value if value is not None else base_types.UninitialisedField(self, 'MntncSvc', DataSetCategory19Code, True)

	@MntncSvc.deleter
	def MntncSvc(self):
		del self._MntncSvc
		self._MntncSvc = base_types.UninitialisedField(self, 'MntncSvc', DataSetCategory19Code, True)

	@property
	def POIIdAssoctn(self):
		return self._POIIdAssoctn

	@POIIdAssoctn.setter
	def POIIdAssoctn(self, value):
		self._POIIdAssoctn = value if value is not None else base_types.UninitialisedField(self, 'POIIdAssoctn', MaintenanceIdentificationAssociation1, True)

	@POIIdAssoctn.deleter
	def POIIdAssoctn(self):
		del self._POIIdAssoctn
		self._POIIdAssoctn = base_types.UninitialisedField(self, 'POIIdAssoctn', MaintenanceIdentificationAssociation1, True)

	@property
	def POISubset(self):
		return self._POISubset

	@POISubset.setter
	def POISubset(self, value):
		self._POISubset = value if value is not None else base_types.UninitialisedField(self, 'POISubset', Max35Text, True)

	@POISubset.deleter
	def POISubset(self):
		del self._POISubset
		self._POISubset = base_types.UninitialisedField(self, 'POISubset', Max35Text, True)

	@property
	def ParamDataSet(self):
		return self._ParamDataSet

	@ParamDataSet.setter
	def ParamDataSet(self, value):
		self._ParamDataSet = value if value is not None else base_types.UninitialisedField(self, 'ParamDataSet', AcceptorConfigurationDataSet7, False)

	@ParamDataSet.deleter
	def ParamDataSet(self):
		del self._ParamDataSet
		self._ParamDataSet = base_types.UninitialisedField(self, 'ParamDataSet', AcceptorConfigurationDataSet7, False)

	@property
	def PrtlDlgtn(self):
		return self._PrtlDlgtn

	@PrtlDlgtn.setter
	def PrtlDlgtn(self, value):
		self._PrtlDlgtn = value if value is not None else base_types.UninitialisedField(self, 'PrtlDlgtn', TrueFalseIndicator, False)

	@PrtlDlgtn.deleter
	def PrtlDlgtn(self):
		del self._PrtlDlgtn
		self._PrtlDlgtn = base_types.UninitialisedField(self, 'PrtlDlgtn', TrueFalseIndicator, False)

	@property
	def SmmtrcKey(self):
		return self._SmmtrcKey

	@SmmtrcKey.setter
	def SmmtrcKey(self, value):
		self._SmmtrcKey = value if value is not None else base_types.UninitialisedField(self, 'SmmtrcKey', CryptographicKey19, True)

	@SmmtrcKey.deleter
	def SmmtrcKey(self):
		del self._SmmtrcKey
		self._SmmtrcKey = base_types.UninitialisedField(self, 'SmmtrcKey', CryptographicKey19, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cert', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlgtdActn', type=MaintenanceDelegateAction11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnScpDef', type=Max3000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnScpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncSvc', type=DataSetCategory19Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIIdAssoctn', type=MaintenanceIdentificationAssociation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POISubset', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ParamDataSet', type=AcceptorConfigurationDataSet7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlDlgtn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SmmtrcKey', type=CryptographicKey19, min=0, max=None, mutex_group=None, array=True),
	))