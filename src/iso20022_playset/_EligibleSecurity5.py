# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._GenericIdentification1 import GenericIdentification1
from ._SecurityIdentification19 import SecurityIdentification19
from ._SystemPartyIdentification2Choice import SystemPartyIdentification2Choice

class EligibleSecurity5(base_types._BaseFieldType):

	__slots__ = ["_CollstnCcy", "_ElgbltySetPrfl", "_PtyId", "_SctyId"]
	@property
	def CollstnCcy(self):
		return self._CollstnCcy

	@CollstnCcy.setter
	def CollstnCcy(self, value):
		self._CollstnCcy = value if type(value) != base_types.auto else self.make_default("CollstnCcy")

	@CollstnCcy.deleter
	def CollstnCcy(self):
		del self._CollstnCcy
		self._CollstnCcy = None

	@property
	def ElgbltySetPrfl(self):
		return self._ElgbltySetPrfl

	@ElgbltySetPrfl.setter
	def ElgbltySetPrfl(self, value):
		self._ElgbltySetPrfl = value if type(value) != base_types.auto else self.make_default("ElgbltySetPrfl")

	@ElgbltySetPrfl.deleter
	def ElgbltySetPrfl(self):
		del self._ElgbltySetPrfl
		self._ElgbltySetPrfl = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollstnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltySetPrfl', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification19, min=1, max=None, mutex_group=None, array=True),
	))