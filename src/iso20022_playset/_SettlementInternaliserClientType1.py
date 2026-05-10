from . import base_types
from .InternalisationData1 import InternalisationData1

class SettlementInternaliserClientType1(base_types._BaseFieldType):

	__slots__ = ["_Rtl", "_Prfssnl"]
	@property
	def Rtl(self):
		return self._Rtl

	@Rtl.setter
	def Rtl(self, value):
		self._Rtl = value if type(value) != base_types.auto else self.make_default("Rtl")

	@Rtl.deleter
	def Rtl(self):
		del self._Rtl
		self._Rtl = None

	@property
	def Prfssnl(self):
		return self._Prfssnl

	@Prfssnl.setter
	def Prfssnl(self, value):
		self._Prfssnl = value if type(value) != base_types.auto else self.make_default("Prfssnl")

	@Prfssnl.deleter
	def Prfssnl(self):
		del self._Prfssnl
		self._Prfssnl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rtl', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prfssnl', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
	))

