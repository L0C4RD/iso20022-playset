# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AdditionalInformation15
from . import CashAssetType1Choice

class CashAsset2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CshAsstTp", "_HldgCcy"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@property
	def CshAsstTp(self):
		return self._CshAsstTp

	@CshAsstTp.setter
	def CshAsstTp(self, value):
		self._CshAsstTp = value if value is not None else base_types.UninitialisedField(self, 'CshAsstTp', CashAssetType1Choice, False)

	@CshAsstTp.deleter
	def CshAsstTp(self):
		del self._CshAsstTp
		self._CshAsstTp = base_types.UninitialisedField(self, 'CshAsstTp', CashAssetType1Choice, False)

	@property
	def HldgCcy(self):
		return self._HldgCcy

	@HldgCcy.setter
	def HldgCcy(self, value):
		self._HldgCcy = value if value is not None else base_types.UninitialisedField(self, 'HldgCcy', ActiveCurrencyCode, False)

	@HldgCcy.deleter
	def HldgCcy(self):
		del self._HldgCcy
		self._HldgCcy = base_types.UninitialisedField(self, 'HldgCcy', ActiveCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAsstTp', type=CashAssetType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))