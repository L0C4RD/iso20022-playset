# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyIdentification253Choice import PartyIdentification253Choice
from ._PartyIdentificationAndAccount227 import PartyIdentificationAndAccount227
from ._SecuritiesAccount18 import SecuritiesAccount18
from ._TradeLeg12 import TradeLeg12

class TradeLegStatement4(base_types._BaseFieldType):

	__slots__ = ["_ClrAcct", "_ClrSgmt", "_NonClrMmb", "_TradLegsDtls"]
	@property
	def ClrAcct(self):
		return self._ClrAcct

	@ClrAcct.setter
	def ClrAcct(self, value):
		self._ClrAcct = value if type(value) != base_types.auto else self.make_default("ClrAcct")

	@ClrAcct.deleter
	def ClrAcct(self):
		del self._ClrAcct
		self._ClrAcct = None

	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if type(value) != base_types.auto else self.make_default("ClrSgmt")

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = None

	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if type(value) != base_types.auto else self.make_default("NonClrMmb")

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = None

	@property
	def TradLegsDtls(self):
		return self._TradLegsDtls

	@TradLegsDtls.setter
	def TradLegsDtls(self, value):
		self._TradLegsDtls = value if type(value) != base_types.auto else self.make_default("TradLegsDtls")

	@TradLegsDtls.deleter
	def TradLegsDtls(self):
		del self._TradLegsDtls
		self._TradLegsDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrAcct', type=SecuritiesAccount18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification253Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount227, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLegsDtls', type=TradeLeg12, min=1, max=None, mutex_group=None, array=True),
	))