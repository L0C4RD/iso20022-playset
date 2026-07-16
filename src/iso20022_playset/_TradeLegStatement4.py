# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification253Choice
from . import PartyIdentificationAndAccount227
from . import SecuritiesAccount18
from . import TradeLeg12

class TradeLegStatement4(base_types._BaseFieldType):

	__slots__ = ["_ClrAcct", "_ClrSgmt", "_NonClrMmb", "_TradLegsDtls"]
	@property
	def ClrAcct(self):
		return self._ClrAcct

	@ClrAcct.setter
	def ClrAcct(self, value):
		self._ClrAcct = value if value is not None else base_types.UninitialisedField(self, 'ClrAcct', SecuritiesAccount18, False)

	@ClrAcct.deleter
	def ClrAcct(self):
		del self._ClrAcct
		self._ClrAcct = base_types.UninitialisedField(self, 'ClrAcct', SecuritiesAccount18, False)

	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if value is not None else base_types.UninitialisedField(self, 'ClrSgmt', PartyIdentification253Choice, False)

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = base_types.UninitialisedField(self, 'ClrSgmt', PartyIdentification253Choice, False)

	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if value is not None else base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount227, False)

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount227, False)

	@property
	def TradLegsDtls(self):
		return self._TradLegsDtls

	@TradLegsDtls.setter
	def TradLegsDtls(self, value):
		self._TradLegsDtls = value if value is not None else base_types.UninitialisedField(self, 'TradLegsDtls', TradeLeg12, True)

	@TradLegsDtls.deleter
	def TradLegsDtls(self):
		del self._TradLegsDtls
		self._TradLegsDtls = base_types.UninitialisedField(self, 'TradLegsDtls', TradeLeg12, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrAcct', type=SecuritiesAccount18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification253Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount227, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLegsDtls', type=TradeLeg12, min=1, max=None, mutex_group=None, array=True),
	))