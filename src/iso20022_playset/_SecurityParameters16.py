# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CryptographicKey18
from . import Max140Binary
from . import Max256Text
from . import TerminalManagementAction3Code

class SecurityParameters16(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_POIChllng", "_SctyElmt", "_TMChllng", "_Vrsn"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@property
	def POIChllng(self):
		return self._POIChllng

	@POIChllng.setter
	def POIChllng(self, value):
		self._POIChllng = value if value is not None else base_types.UninitialisedField(self, 'POIChllng', Max140Binary, False)

	@POIChllng.deleter
	def POIChllng(self):
		del self._POIChllng
		self._POIChllng = base_types.UninitialisedField(self, 'POIChllng', Max140Binary, False)

	@property
	def SctyElmt(self):
		return self._SctyElmt

	@SctyElmt.setter
	def SctyElmt(self, value):
		self._SctyElmt = value if value is not None else base_types.UninitialisedField(self, 'SctyElmt', CryptographicKey18, True)

	@SctyElmt.deleter
	def SctyElmt(self):
		del self._SctyElmt
		self._SctyElmt = base_types.UninitialisedField(self, 'SctyElmt', CryptographicKey18, True)

	@property
	def TMChllng(self):
		return self._TMChllng

	@TMChllng.setter
	def TMChllng(self, value):
		self._TMChllng = value if value is not None else base_types.UninitialisedField(self, 'TMChllng', Max140Binary, False)

	@TMChllng.deleter
	def TMChllng(self):
		del self._TMChllng
		self._TMChllng = base_types.UninitialisedField(self, 'TMChllng', Max140Binary, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyElmt', type=CryptographicKey18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
	))