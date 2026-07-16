# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TaxExemptionReasonFormat1Choice

class TaxParty4(base_types._BaseFieldType):

	__slots__ = ["_RegnId", "_TaxId", "_TaxTp", "_TaxXmptnRsn"]
	@property
	def RegnId(self):
		return self._RegnId

	@RegnId.setter
	def RegnId(self, value):
		self._RegnId = value if value is not None else base_types.UninitialisedField(self, 'RegnId', Max35Text, False)

	@RegnId.deleter
	def RegnId(self):
		del self._RegnId
		self._RegnId = base_types.UninitialisedField(self, 'RegnId', Max35Text, False)

	@property
	def TaxId(self):
		return self._TaxId

	@TaxId.setter
	def TaxId(self, value):
		self._TaxId = value if value is not None else base_types.UninitialisedField(self, 'TaxId', Max35Text, False)

	@TaxId.deleter
	def TaxId(self):
		del self._TaxId
		self._TaxId = base_types.UninitialisedField(self, 'TaxId', Max35Text, False)

	@property
	def TaxTp(self):
		return self._TaxTp

	@TaxTp.setter
	def TaxTp(self, value):
		self._TaxTp = value if value is not None else base_types.UninitialisedField(self, 'TaxTp', Max35Text, False)

	@TaxTp.deleter
	def TaxTp(self):
		del self._TaxTp
		self._TaxTp = base_types.UninitialisedField(self, 'TaxTp', Max35Text, False)

	@property
	def TaxXmptnRsn(self):
		return self._TaxXmptnRsn

	@TaxXmptnRsn.setter
	def TaxXmptnRsn(self, value):
		self._TaxXmptnRsn = value if value is not None else base_types.UninitialisedField(self, 'TaxXmptnRsn', TaxExemptionReasonFormat1Choice, True)

	@TaxXmptnRsn.deleter
	def TaxXmptnRsn(self):
		del self._TaxXmptnRsn
		self._TaxXmptnRsn = base_types.UninitialisedField(self, 'TaxXmptnRsn', TaxExemptionReasonFormat1Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxXmptnRsn', type=TaxExemptionReasonFormat1Choice, min=0, max=None, mutex_group=None, array=True),
	))