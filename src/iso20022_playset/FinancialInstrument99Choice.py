from . import base_types
from .ISINOct2015Identifier import ISINOct2015Identifier

class FinancialInstrument99Choice(base_types._BaseFieldType):

	__slots__ = ["_StrtgyInstrms", "_Id"]
	@property
	def StrtgyInstrms(self):
		return self._StrtgyInstrms

	@StrtgyInstrms.setter
	def StrtgyInstrms(self, value):
		self._StrtgyInstrms = value if type(value) != base_types.auto else self.make_default("StrtgyInstrms")

	@StrtgyInstrms.deleter
	def StrtgyInstrms(self):
		del self._StrtgyInstrms
		self._StrtgyInstrms = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StrtgyInstrms', type=ISINOct2015Identifier, min=2, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
	))

