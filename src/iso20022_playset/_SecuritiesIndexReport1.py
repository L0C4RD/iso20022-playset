from . import base_types
from ._CountryCode import CountryCode
from ._FinancialInstrument46Choice import FinancialInstrument46Choice
from ._Max35Text import Max35Text
from ._Period4Choice import Period4Choice

class SecuritiesIndexReport1(base_types._BaseFieldType):

	__slots__ = ["_Indx", "_RqstngNtty", "_TechRcrdId", "_VldtyPrd"]
	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if type(value) != base_types.auto else self.make_default("Indx")

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = None

	@property
	def RqstngNtty(self):
		return self._RqstngNtty

	@RqstngNtty.setter
	def RqstngNtty(self, value):
		self._RqstngNtty = value if type(value) != base_types.auto else self.make_default("RqstngNtty")

	@RqstngNtty.deleter
	def RqstngNtty(self):
		del self._RqstngNtty
		self._RqstngNtty = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if type(value) != base_types.auto else self.make_default("VldtyPrd")

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Indx', type=FinancialInstrument46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RqstngNtty', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
	))

