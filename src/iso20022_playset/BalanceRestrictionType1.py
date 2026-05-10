from . import base_types
import ProcessingType1Choice
import GenericIdentification1
import Max140Text

class BalanceRestrictionType1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Desc", "_PrcgTp"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def PrcgTp(self):
		return self._PrcgTp

	@PrcgTp.setter
	def PrcgTp(self, value):
		self._PrcgTp = value if type(value) != auto else self.make_default("PrcgTp")

	@PrcgTp.deleter
	def PrcgTp(self):
		del self._PrcgTp
		self._PrcgTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=GenericIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgTp', type=ProcessingType1Choice, min=0, max=1, mutex_group=None, array=False),
	))

