# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISINOct2015Identifier import ISINOct2015Identifier

class FinancialInstrument99Choice(base_types._BaseFieldType):

	__slots__ = ["_Id", "_StrtgyInstrms"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StrtgyInstrms', type=ISINOct2015Identifier, min=2, max=None, mutex_group=1, array=True),
	))