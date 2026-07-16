# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Number

class RejectedElement1(base_types._BaseFieldType):

	__slots__ = ["_ElmtSeqNb", "_IndvRjctnRsn"]
	@property
	def ElmtSeqNb(self):
		return self._ElmtSeqNb

	@ElmtSeqNb.setter
	def ElmtSeqNb(self, value):
		self._ElmtSeqNb = value if value is not None else base_types.UninitialisedField(self, 'ElmtSeqNb', Number, False)

	@ElmtSeqNb.deleter
	def ElmtSeqNb(self):
		del self._ElmtSeqNb
		self._ElmtSeqNb = base_types.UninitialisedField(self, 'ElmtSeqNb', Number, False)

	@property
	def IndvRjctnRsn(self):
		return self._IndvRjctnRsn

	@IndvRjctnRsn.setter
	def IndvRjctnRsn(self, value):
		self._IndvRjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'IndvRjctnRsn', Max140Text, False)

	@IndvRjctnRsn.deleter
	def IndvRjctnRsn(self):
		del self._IndvRjctnRsn
		self._IndvRjctnRsn = base_types.UninitialisedField(self, 'IndvRjctnRsn', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElmtSeqNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvRjctnRsn', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))