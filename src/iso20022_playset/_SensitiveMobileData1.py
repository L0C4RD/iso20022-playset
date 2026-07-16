# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35NumericText

class SensitiveMobileData1(base_types._BaseFieldType):

	__slots__ = ["_IMEI", "_IMSI", "_MSISDN"]
	@property
	def IMEI(self):
		return self._IMEI

	@IMEI.setter
	def IMEI(self, value):
		self._IMEI = value if value is not None else base_types.UninitialisedField(self, 'IMEI', Max35NumericText, False)

	@IMEI.deleter
	def IMEI(self):
		del self._IMEI
		self._IMEI = base_types.UninitialisedField(self, 'IMEI', Max35NumericText, False)

	@property
	def IMSI(self):
		return self._IMSI

	@IMSI.setter
	def IMSI(self, value):
		self._IMSI = value if value is not None else base_types.UninitialisedField(self, 'IMSI', Max35NumericText, False)

	@IMSI.deleter
	def IMSI(self):
		del self._IMSI
		self._IMSI = base_types.UninitialisedField(self, 'IMSI', Max35NumericText, False)

	@property
	def MSISDN(self):
		return self._MSISDN

	@MSISDN.setter
	def MSISDN(self, value):
		self._MSISDN = value if value is not None else base_types.UninitialisedField(self, 'MSISDN', Max35NumericText, False)

	@MSISDN.deleter
	def MSISDN(self):
		del self._MSISDN
		self._MSISDN = base_types.UninitialisedField(self, 'MSISDN', Max35NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IMEI', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IMSI', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MSISDN', type=Max35NumericText, min=1, max=1, mutex_group=None, array=False),
	))