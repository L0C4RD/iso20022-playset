from . import base_types
from .Max35Text import Max35Text
from .RetailerService2Code import RetailerService2Code
from .RetailerService8Code import RetailerService8Code
from .Max1025Text import Max1025Text
from .RetailerMessage1Code import RetailerMessage1Code
from .TerminalManagementAction3Code import TerminalManagementAction3Code
from .Max256Text import Max256Text
from .Organisation26 import Organisation26

class SaleToPOIProtocolParameter3(base_types._BaseFieldType):

	__slots__ = ["_MrchntId", "_AllwdPOISvc", "_AllwdPOIMsg", "_AllwdSaleDvc", "_XtrnlyTpSpprtd", "_HstId", "_ActnTp", "_AllwdSaleMsg", "_SaleId", "_Vrsn", "_MrchntPOIId"]
	@property
	def MrchntId(self):
		return self._MrchntId

	@MrchntId.setter
	def MrchntId(self, value):
		self._MrchntId = value if type(value) != auto else self.make_default("MrchntId")

	@MrchntId.deleter
	def MrchntId(self):
		del self._MrchntId
		self._MrchntId = None

	@property
	def AllwdPOISvc(self):
		return self._AllwdPOISvc

	@AllwdPOISvc.setter
	def AllwdPOISvc(self, value):
		self._AllwdPOISvc = value if type(value) != auto else self.make_default("AllwdPOISvc")

	@AllwdPOISvc.deleter
	def AllwdPOISvc(self):
		del self._AllwdPOISvc
		self._AllwdPOISvc = None

	@property
	def AllwdPOIMsg(self):
		return self._AllwdPOIMsg

	@AllwdPOIMsg.setter
	def AllwdPOIMsg(self, value):
		self._AllwdPOIMsg = value if type(value) != auto else self.make_default("AllwdPOIMsg")

	@AllwdPOIMsg.deleter
	def AllwdPOIMsg(self):
		del self._AllwdPOIMsg
		self._AllwdPOIMsg = None

	@property
	def AllwdSaleDvc(self):
		return self._AllwdSaleDvc

	@AllwdSaleDvc.setter
	def AllwdSaleDvc(self, value):
		self._AllwdSaleDvc = value if type(value) != auto else self.make_default("AllwdSaleDvc")

	@AllwdSaleDvc.deleter
	def AllwdSaleDvc(self):
		del self._AllwdSaleDvc
		self._AllwdSaleDvc = None

	@property
	def XtrnlyTpSpprtd(self):
		return self._XtrnlyTpSpprtd

	@XtrnlyTpSpprtd.setter
	def XtrnlyTpSpprtd(self, value):
		self._XtrnlyTpSpprtd = value if type(value) != auto else self.make_default("XtrnlyTpSpprtd")

	@XtrnlyTpSpprtd.deleter
	def XtrnlyTpSpprtd(self):
		del self._XtrnlyTpSpprtd
		self._XtrnlyTpSpprtd = None

	@property
	def HstId(self):
		return self._HstId

	@HstId.setter
	def HstId(self, value):
		self._HstId = value if type(value) != auto else self.make_default("HstId")

	@HstId.deleter
	def HstId(self):
		del self._HstId
		self._HstId = None

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def AllwdSaleMsg(self):
		return self._AllwdSaleMsg

	@AllwdSaleMsg.setter
	def AllwdSaleMsg(self, value):
		self._AllwdSaleMsg = value if type(value) != auto else self.make_default("AllwdSaleMsg")

	@AllwdSaleMsg.deleter
	def AllwdSaleMsg(self):
		del self._AllwdSaleMsg
		self._AllwdSaleMsg = None

	@property
	def SaleId(self):
		return self._SaleId

	@SaleId.setter
	def SaleId(self, value):
		self._SaleId = value if type(value) != auto else self.make_default("SaleId")

	@SaleId.deleter
	def SaleId(self):
		del self._SaleId
		self._SaleId = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def MrchntPOIId(self):
		return self._MrchntPOIId

	@MrchntPOIId.setter
	def MrchntPOIId(self, value):
		self._MrchntPOIId = value if type(value) != auto else self.make_default("MrchntPOIId")

	@MrchntPOIId.deleter
	def MrchntPOIId(self):
		del self._MrchntPOIId
		self._MrchntPOIId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrchntId', type=Organisation26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllwdPOISvc', type=RetailerService2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllwdPOIMsg', type=RetailerMessage1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllwdSaleDvc', type=RetailerService8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XtrnlyTpSpprtd', type=Max1025Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HstId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllwdSaleMsg', type=RetailerMessage1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntPOIId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

