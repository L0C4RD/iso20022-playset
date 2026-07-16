# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import Max35Text

class LegalMandate1(base_types._BaseFieldType):

	__slots__ = ["_Dsclmr", "_Prgrph"]
	@property
	def Dsclmr(self):
		return self._Dsclmr

	@Dsclmr.setter
	def Dsclmr(self, value):
		self._Dsclmr = value if value is not None else base_types.UninitialisedField(self, 'Dsclmr', Max350Text, False)

	@Dsclmr.deleter
	def Dsclmr(self):
		del self._Dsclmr
		self._Dsclmr = base_types.UninitialisedField(self, 'Dsclmr', Max350Text, False)

	@property
	def Prgrph(self):
		return self._Prgrph

	@Prgrph.setter
	def Prgrph(self, value):
		self._Prgrph = value if value is not None else base_types.UninitialisedField(self, 'Prgrph', Max35Text, False)

	@Prgrph.deleter
	def Prgrph(self):
		del self._Prgrph
		self._Prgrph = base_types.UninitialisedField(self, 'Prgrph', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dsclmr', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrph', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))