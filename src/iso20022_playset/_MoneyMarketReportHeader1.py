# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod1
from . import LEIIdentifier

class MoneyMarketReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_RefPrd", "_RptgAgt"]
	@property
	def RefPrd(self):
		return self._RefPrd

	@RefPrd.setter
	def RefPrd(self, value):
		self._RefPrd = value if value is not None else base_types.UninitialisedField(self, 'RefPrd', DateTimePeriod1, False)

	@RefPrd.deleter
	def RefPrd(self):
		del self._RefPrd
		self._RefPrd = base_types.UninitialisedField(self, 'RefPrd', DateTimePeriod1, False)

	@property
	def RptgAgt(self):
		return self._RptgAgt

	@RptgAgt.setter
	def RptgAgt(self, value):
		self._RptgAgt = value if value is not None else base_types.UninitialisedField(self, 'RptgAgt', LEIIdentifier, False)

	@RptgAgt.deleter
	def RptgAgt(self):
		del self._RptgAgt
		self._RptgAgt = base_types.UninitialisedField(self, 'RptgAgt', LEIIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RefPrd', type=DateTimePeriod1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgAgt', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
	))