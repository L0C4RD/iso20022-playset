# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CFIOct2015Identifier
from . import GenericIdentification3

class SecurityClassificationType2Choice(base_types._BaseFieldType):

	__slots__ = ["_AltrnClssfctn", "_CFI"]
	@property
	def AltrnClssfctn(self):
		return self._AltrnClssfctn

	@AltrnClssfctn.setter
	def AltrnClssfctn(self, value):
		self._AltrnClssfctn = value if value is not None else base_types.UninitialisedField(self, 'AltrnClssfctn', GenericIdentification3, False)

	@AltrnClssfctn.deleter
	def AltrnClssfctn(self):
		del self._AltrnClssfctn
		self._AltrnClssfctn = base_types.UninitialisedField(self, 'AltrnClssfctn', GenericIdentification3, False)

	@property
	def CFI(self):
		return self._CFI

	@CFI.setter
	def CFI(self, value):
		self._CFI = value if value is not None else base_types.UninitialisedField(self, 'CFI', CFIOct2015Identifier, False)

	@CFI.deleter
	def CFI(self):
		del self._CFI
		self._CFI = base_types.UninitialisedField(self, 'CFI', CFIOct2015Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnClssfctn', type=GenericIdentification3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CFI', type=CFIOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
	))