# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO3NumericCountryCode
from . import Max140Text
from . import Max35Text
from . import Max70Text
from . import Min3Max4Text

class Organisation26(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_CmonNm", "_CtryCd", "_MrchntCtgyCd", "_RegdIdr"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Max140Text, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Max140Text, False)

	@property
	def CmonNm(self):
		return self._CmonNm

	@CmonNm.setter
	def CmonNm(self, value):
		self._CmonNm = value if value is not None else base_types.UninitialisedField(self, 'CmonNm', Max70Text, False)

	@CmonNm.deleter
	def CmonNm(self):
		del self._CmonNm
		self._CmonNm = base_types.UninitialisedField(self, 'CmonNm', Max70Text, False)

	@property
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if value is not None else base_types.UninitialisedField(self, 'CtryCd', ISO3NumericCountryCode, False)

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = base_types.UninitialisedField(self, 'CtryCd', ISO3NumericCountryCode, False)

	@property
	def MrchntCtgyCd(self):
		return self._MrchntCtgyCd

	@MrchntCtgyCd.setter
	def MrchntCtgyCd(self, value):
		self._MrchntCtgyCd = value if value is not None else base_types.UninitialisedField(self, 'MrchntCtgyCd', Min3Max4Text, False)

	@MrchntCtgyCd.deleter
	def MrchntCtgyCd(self):
		del self._MrchntCtgyCd
		self._MrchntCtgyCd = base_types.UninitialisedField(self, 'MrchntCtgyCd', Min3Max4Text, False)

	@property
	def RegdIdr(self):
		return self._RegdIdr

	@RegdIdr.setter
	def RegdIdr(self, value):
		self._RegdIdr = value if value is not None else base_types.UninitialisedField(self, 'RegdIdr', Max35Text, False)

	@RegdIdr.deleter
	def RegdIdr(self):
		del self._RegdIdr
		self._RegdIdr = base_types.UninitialisedField(self, 'RegdIdr', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonNm', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryCd', type=ISO3NumericCountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=Min3Max4Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))