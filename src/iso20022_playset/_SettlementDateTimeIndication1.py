# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime

class SettlementDateTimeIndication1(base_types._BaseFieldType):

	__slots__ = ["_CdtDtTm", "_DbtDtTm"]
	@property
	def CdtDtTm(self):
		return self._CdtDtTm

	@CdtDtTm.setter
	def CdtDtTm(self, value):
		self._CdtDtTm = value if value is not None else base_types.UninitialisedField(self, 'CdtDtTm', ISODateTime, False)

	@CdtDtTm.deleter
	def CdtDtTm(self):
		del self._CdtDtTm
		self._CdtDtTm = base_types.UninitialisedField(self, 'CdtDtTm', ISODateTime, False)

	@property
	def DbtDtTm(self):
		return self._DbtDtTm

	@DbtDtTm.setter
	def DbtDtTm(self, value):
		self._DbtDtTm = value if value is not None else base_types.UninitialisedField(self, 'DbtDtTm', ISODateTime, False)

	@DbtDtTm.deleter
	def DbtDtTm(self):
		del self._DbtDtTm
		self._DbtDtTm = base_types.UninitialisedField(self, 'DbtDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))