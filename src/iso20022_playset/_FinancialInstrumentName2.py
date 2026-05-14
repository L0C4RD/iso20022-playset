# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text

class FinancialInstrumentName2(base_types._BaseFieldType):

	__slots__ = ["_ISOLngNm", "_ISOShrtNm", "_VldFr"]
	@property
	def ISOLngNm(self):
		return self._ISOLngNm

	@ISOLngNm.setter
	def ISOLngNm(self, value):
		self._ISOLngNm = value if type(value) != base_types.auto else self.make_default("ISOLngNm")

	@ISOLngNm.deleter
	def ISOLngNm(self):
		del self._ISOLngNm
		self._ISOLngNm = None

	@property
	def ISOShrtNm(self):
		return self._ISOShrtNm

	@ISOShrtNm.setter
	def ISOShrtNm(self, value):
		self._ISOShrtNm = value if type(value) != base_types.auto else self.make_default("ISOShrtNm")

	@ISOShrtNm.deleter
	def ISOShrtNm(self):
		del self._ISOShrtNm
		self._ISOShrtNm = None

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if type(value) != base_types.auto else self.make_default("VldFr")

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISOLngNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISOShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))