from . import base_types
import Max140Text
import Min3Max4Text
import Max35Text
import ISO3NumericCountryCode
import Max70Text

class Organisation26(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_CtryCd", "_CmonNm", "_MrchntCtgyCd", "_RegdIdr"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if type(value) != auto else self.make_default("CtryCd")

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = None

	@property
	def CmonNm(self):
		return self._CmonNm

	@CmonNm.setter
	def CmonNm(self, value):
		self._CmonNm = value if type(value) != auto else self.make_default("CmonNm")

	@CmonNm.deleter
	def CmonNm(self):
		del self._CmonNm
		self._CmonNm = None

	@property
	def MrchntCtgyCd(self):
		return self._MrchntCtgyCd

	@MrchntCtgyCd.setter
	def MrchntCtgyCd(self, value):
		self._MrchntCtgyCd = value if type(value) != auto else self.make_default("MrchntCtgyCd")

	@MrchntCtgyCd.deleter
	def MrchntCtgyCd(self):
		del self._MrchntCtgyCd
		self._MrchntCtgyCd = None

	@property
	def RegdIdr(self):
		return self._RegdIdr

	@RegdIdr.setter
	def RegdIdr(self, value):
		self._RegdIdr = value if type(value) != auto else self.make_default("RegdIdr")

	@RegdIdr.deleter
	def RegdIdr(self):
		del self._RegdIdr
		self._RegdIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryCd', type=ISO3NumericCountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonNm', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=Min3Max4Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

