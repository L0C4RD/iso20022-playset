from . import base_types
from ._Purpose3Choice import Purpose3Choice
from ._CountryCode import CountryCode
from ._ClassificationType1Choice import ClassificationType1Choice

class MarketIdentification87(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_SttlmPurp", "_ClssfctnTp"]
	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != base_types.auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def SttlmPurp(self):
		return self._SttlmPurp

	@SttlmPurp.setter
	def SttlmPurp(self, value):
		self._SttlmPurp = value if type(value) != base_types.auto else self.make_default("SttlmPurp")

	@SttlmPurp.deleter
	def SttlmPurp(self):
		del self._SttlmPurp
		self._SttlmPurp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPurp', type=Purpose3Choice, min=0, max=1, mutex_group=None, array=False),
	))

