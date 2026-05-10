import base_types
import Max140Text
import Number

class RejectedElement1(base_types._BaseFieldType):

	__slots__ = ["_IndvRjctnRsn", "_ElmtSeqNb"]
	@property
	def IndvRjctnRsn(self):
		return self._IndvRjctnRsn

	@IndvRjctnRsn.setter
	def IndvRjctnRsn(self, value):
		self._IndvRjctnRsn = value if type(value) != auto else self.make_default("IndvRjctnRsn")

	@IndvRjctnRsn.deleter
	def IndvRjctnRsn(self):
		del self._IndvRjctnRsn
		self._IndvRjctnRsn = None

	@property
	def ElmtSeqNb(self):
		return self._ElmtSeqNb

	@ElmtSeqNb.setter
	def ElmtSeqNb(self, value):
		self._ElmtSeqNb = value if type(value) != auto else self.make_default("ElmtSeqNb")

	@ElmtSeqNb.deleter
	def ElmtSeqNb(self):
		del self._ElmtSeqNb
		self._ElmtSeqNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndvRjctnRsn', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtSeqNb', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

