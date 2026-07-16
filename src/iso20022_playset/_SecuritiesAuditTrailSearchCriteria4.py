# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriodSearch1Choice
from . import SecurityIdentification39

class SecuritiesAuditTrailSearchCriteria4(base_types._BaseFieldType):

	__slots__ = ["_DtPrd", "_FinInstrmId"]
	@property
	def DtPrd(self):
		return self._DtPrd

	@DtPrd.setter
	def DtPrd(self, value):
		self._DtPrd = value if value is not None else base_types.UninitialisedField(self, 'DtPrd', DatePeriodSearch1Choice, False)

	@DtPrd.deleter
	def DtPrd(self):
		del self._DtPrd
		self._DtPrd = base_types.UninitialisedField(self, 'DtPrd', DatePeriodSearch1Choice, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification39, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification39, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtPrd', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification39, min=0, max=1, mutex_group=None, array=False),
	))