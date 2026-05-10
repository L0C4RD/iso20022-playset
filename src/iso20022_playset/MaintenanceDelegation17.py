import base_types
import TerminalManagementAction3Code
import MaintenanceIdentificationAssociation1
import Max5000Binary
import Max3000Binary
import ContentInformationType39
import Max35Text
import DataSetCategory19Code
import Response2Code

class MaintenanceDelegation17(base_types._BaseFieldType):

	__slots__ = ["_RspnRsn", "_POIIdAssoctn", "_DlgtnScpDef", "_Rspn", "_POISubset", "_PrtctdDlgtnProof", "_DlgtnTp", "_DlgtnScpId", "_MntncSvc", "_DlgtnProof"]
	@property
	def RspnRsn(self):
		return self._RspnRsn

	@RspnRsn.setter
	def RspnRsn(self, value):
		self._RspnRsn = value if type(value) != auto else self.make_default("RspnRsn")

	@RspnRsn.deleter
	def RspnRsn(self):
		del self._RspnRsn
		self._RspnRsn = None

	@property
	def POIIdAssoctn(self):
		return self._POIIdAssoctn

	@POIIdAssoctn.setter
	def POIIdAssoctn(self, value):
		self._POIIdAssoctn = value if type(value) != auto else self.make_default("POIIdAssoctn")

	@POIIdAssoctn.deleter
	def POIIdAssoctn(self):
		del self._POIIdAssoctn
		self._POIIdAssoctn = None

	@property
	def DlgtnScpDef(self):
		return self._DlgtnScpDef

	@DlgtnScpDef.setter
	def DlgtnScpDef(self, value):
		self._DlgtnScpDef = value if type(value) != auto else self.make_default("DlgtnScpDef")

	@DlgtnScpDef.deleter
	def DlgtnScpDef(self):
		del self._DlgtnScpDef
		self._DlgtnScpDef = None

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

	@property
	def POISubset(self):
		return self._POISubset

	@POISubset.setter
	def POISubset(self, value):
		self._POISubset = value if type(value) != auto else self.make_default("POISubset")

	@POISubset.deleter
	def POISubset(self):
		del self._POISubset
		self._POISubset = None

	@property
	def PrtctdDlgtnProof(self):
		return self._PrtctdDlgtnProof

	@PrtctdDlgtnProof.setter
	def PrtctdDlgtnProof(self, value):
		self._PrtctdDlgtnProof = value if type(value) != auto else self.make_default("PrtctdDlgtnProof")

	@PrtctdDlgtnProof.deleter
	def PrtctdDlgtnProof(self):
		del self._PrtctdDlgtnProof
		self._PrtctdDlgtnProof = None

	@property
	def DlgtnTp(self):
		return self._DlgtnTp

	@DlgtnTp.setter
	def DlgtnTp(self, value):
		self._DlgtnTp = value if type(value) != auto else self.make_default("DlgtnTp")

	@DlgtnTp.deleter
	def DlgtnTp(self):
		del self._DlgtnTp
		self._DlgtnTp = None

	@property
	def DlgtnScpId(self):
		return self._DlgtnScpId

	@DlgtnScpId.setter
	def DlgtnScpId(self, value):
		self._DlgtnScpId = value if type(value) != auto else self.make_default("DlgtnScpId")

	@DlgtnScpId.deleter
	def DlgtnScpId(self):
		del self._DlgtnScpId
		self._DlgtnScpId = None

	@property
	def MntncSvc(self):
		return self._MntncSvc

	@MntncSvc.setter
	def MntncSvc(self, value):
		self._MntncSvc = value if type(value) != auto else self.make_default("MntncSvc")

	@MntncSvc.deleter
	def MntncSvc(self):
		del self._MntncSvc
		self._MntncSvc = None

	@property
	def DlgtnProof(self):
		return self._DlgtnProof

	@DlgtnProof.setter
	def DlgtnProof(self, value):
		self._DlgtnProof = value if type(value) != auto else self.make_default("DlgtnProof")

	@DlgtnProof.deleter
	def DlgtnProof(self):
		del self._DlgtnProof
		self._DlgtnProof = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspnRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIIdAssoctn', type=MaintenanceIdentificationAssociation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlgtnScpDef', type=Max3000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=Response2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POISubset', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdDlgtnProof', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnScpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncSvc', type=DataSetCategory19Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlgtnProof', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
	))

