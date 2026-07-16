# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CFIOct2015Identifier
from . import ISODate
from . import Modification1Code
from . import Period4Choice

class SecuritiesInstrumentClassification2(base_types._BaseFieldType):

	__slots__ = ["_Idr", "_LastUpdtd", "_Mod", "_VldtyPrd"]
	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if value is not None else base_types.UninitialisedField(self, 'Idr', CFIOct2015Identifier, False)

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = base_types.UninitialisedField(self, 'Idr', CFIOct2015Identifier, False)

	@property
	def LastUpdtd(self):
		return self._LastUpdtd

	@LastUpdtd.setter
	def LastUpdtd(self, value):
		self._LastUpdtd = value if value is not None else base_types.UninitialisedField(self, 'LastUpdtd', ISODate, False)

	@LastUpdtd.deleter
	def LastUpdtd(self):
		del self._LastUpdtd
		self._LastUpdtd = base_types.UninitialisedField(self, 'LastUpdtd', ISODate, False)

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if value is not None else base_types.UninitialisedField(self, 'Mod', Modification1Code, False)

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = base_types.UninitialisedField(self, 'Mod', Modification1Code, False)

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if value is not None else base_types.UninitialisedField(self, 'VldtyPrd', Period4Choice, False)

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = base_types.UninitialisedField(self, 'VldtyPrd', Period4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Idr', type=CFIOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastUpdtd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
	))