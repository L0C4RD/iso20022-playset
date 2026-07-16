# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import SecurityIdentification39

class FinancialInstrumentIdentificationValidity3(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_ISINVldFr"]
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

	@property
	def ISINVldFr(self):
		return self._ISINVldFr

	@ISINVldFr.setter
	def ISINVldFr(self, value):
		self._ISINVldFr = value if value is not None else base_types.UninitialisedField(self, 'ISINVldFr', ISODate, False)

	@ISINVldFr.deleter
	def ISINVldFr(self):
		del self._ISINVldFr
		self._ISINVldFr = base_types.UninitialisedField(self, 'ISINVldFr', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISINVldFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))