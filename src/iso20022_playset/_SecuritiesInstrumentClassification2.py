# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CFIOct2015Identifier import CFIOct2015Identifier
from ._ISODate import ISODate
from ._Modification1Code import Modification1Code
from ._Period4Choice import Period4Choice

class SecuritiesInstrumentClassification2(base_types._BaseFieldType):

	__slots__ = ["_Idr", "_LastUpdtd", "_Mod", "_VldtyPrd"]
	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if type(value) != base_types.auto else self.make_default("Idr")

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = None

	@property
	def LastUpdtd(self):
		return self._LastUpdtd

	@LastUpdtd.setter
	def LastUpdtd(self, value):
		self._LastUpdtd = value if type(value) != base_types.auto else self.make_default("LastUpdtd")

	@LastUpdtd.deleter
	def LastUpdtd(self):
		del self._LastUpdtd
		self._LastUpdtd = None

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != base_types.auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if type(value) != base_types.auto else self.make_default("VldtyPrd")

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Idr', type=CFIOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastUpdtd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
	))