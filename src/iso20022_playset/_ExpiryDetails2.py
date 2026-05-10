from . import base_types
from .Max2000Text import Max2000Text
from .ExpiryTerms2 import ExpiryTerms2

class ExpiryDetails2(base_types._BaseFieldType):

	__slots__ = ["_AddtlXpryInf", "_XpryTerms"]
	@property
	def AddtlXpryInf(self):
		return self._AddtlXpryInf

	@AddtlXpryInf.setter
	def AddtlXpryInf(self, value):
		self._AddtlXpryInf = value if type(value) != base_types.auto else self.make_default("AddtlXpryInf")

	@AddtlXpryInf.deleter
	def AddtlXpryInf(self):
		del self._AddtlXpryInf
		self._AddtlXpryInf = None

	@property
	def XpryTerms(self):
		return self._XpryTerms

	@XpryTerms.setter
	def XpryTerms(self, value):
		self._XpryTerms = value if type(value) != base_types.auto else self.make_default("XpryTerms")

	@XpryTerms.deleter
	def XpryTerms(self):
		del self._XpryTerms
		self._XpryTerms = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlXpryInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpryTerms', type=ExpiryTerms2, min=0, max=1, mutex_group=None, array=False),
	))

