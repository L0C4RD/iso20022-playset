# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import GenericIdentification1
from . import SecurityIdentification19
from . import SystemPartyIdentification2Choice

class EligibleSecurity5(base_types._BaseFieldType):

	__slots__ = ["_CollstnCcy", "_ElgbltySetPrfl", "_PtyId", "_SctyId"]
	@property
	def CollstnCcy(self):
		return self._CollstnCcy

	@CollstnCcy.setter
	def CollstnCcy(self, value):
		self._CollstnCcy = value if value is not None else base_types.UninitialisedField(self, 'CollstnCcy', ActiveOrHistoricCurrencyCode, False)

	@CollstnCcy.deleter
	def CollstnCcy(self):
		del self._CollstnCcy
		self._CollstnCcy = base_types.UninitialisedField(self, 'CollstnCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def ElgbltySetPrfl(self):
		return self._ElgbltySetPrfl

	@ElgbltySetPrfl.setter
	def ElgbltySetPrfl(self, value):
		self._ElgbltySetPrfl = value if value is not None else base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification1, False)

	@ElgbltySetPrfl.deleter
	def ElgbltySetPrfl(self):
		del self._ElgbltySetPrfl
		self._ElgbltySetPrfl = base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification1, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification2Choice, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification2Choice, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification19, True)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification19, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollstnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltySetPrfl', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification19, min=1, max=None, mutex_group=None, array=True),
	))