# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType39
from . import DataSetCategory19Code
from . import MaintenanceIdentificationAssociation1
from . import Max3000Binary
from . import Max35Text
from . import Max5000Binary
from . import Response2Code
from . import TerminalManagementAction3Code

class MaintenanceDelegation17(base_types._BaseFieldType):

	__slots__ = ["_DlgtnProof", "_DlgtnScpDef", "_DlgtnScpId", "_DlgtnTp", "_MntncSvc", "_POIIdAssoctn", "_POISubset", "_PrtctdDlgtnProof", "_Rspn", "_RspnRsn"]
	@property
	def DlgtnProof(self):
		return self._DlgtnProof

	@DlgtnProof.setter
	def DlgtnProof(self, value):
		self._DlgtnProof = value if value is not None else base_types.UninitialisedField(self, 'DlgtnProof', Max5000Binary, False)

	@DlgtnProof.deleter
	def DlgtnProof(self):
		del self._DlgtnProof
		self._DlgtnProof = base_types.UninitialisedField(self, 'DlgtnProof', Max5000Binary, False)

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
	def PrtctdDlgtnProof(self):
		return self._PrtctdDlgtnProof

	@PrtctdDlgtnProof.setter
	def PrtctdDlgtnProof(self, value):
		self._PrtctdDlgtnProof = value if value is not None else base_types.UninitialisedField(self, 'PrtctdDlgtnProof', ContentInformationType39, False)

	@PrtctdDlgtnProof.deleter
	def PrtctdDlgtnProof(self):
		del self._PrtctdDlgtnProof
		self._PrtctdDlgtnProof = base_types.UninitialisedField(self, 'PrtctdDlgtnProof', ContentInformationType39, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', Response2Code, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', Response2Code, False)

	@property
	def RspnRsn(self):
		return self._RspnRsn

	@RspnRsn.setter
	def RspnRsn(self, value):
		self._RspnRsn = value if value is not None else base_types.UninitialisedField(self, 'RspnRsn', Max35Text, False)

	@RspnRsn.deleter
	def RspnRsn(self):
		del self._RspnRsn
		self._RspnRsn = base_types.UninitialisedField(self, 'RspnRsn', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlgtnProof', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnScpDef', type=Max3000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnScpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncSvc', type=DataSetCategory19Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIIdAssoctn', type=MaintenanceIdentificationAssociation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POISubset', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdDlgtnProof', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=Response2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))