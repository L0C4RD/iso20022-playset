# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CFIOct2015Identifier
from . import GenericIdentification86

class ClassificationType33Choice(base_types._BaseFieldType):

	__slots__ = ["_AltrnClssfctn", "_ClssfctnFinInstrm"]
	@property
	def AltrnClssfctn(self):
		return self._AltrnClssfctn

	@AltrnClssfctn.setter
	def AltrnClssfctn(self, value):
		self._AltrnClssfctn = value if value is not None else base_types.UninitialisedField(self, 'AltrnClssfctn', GenericIdentification86, False)

	@AltrnClssfctn.deleter
	def AltrnClssfctn(self):
		del self._AltrnClssfctn
		self._AltrnClssfctn = base_types.UninitialisedField(self, 'AltrnClssfctn', GenericIdentification86, False)

	@property
	def ClssfctnFinInstrm(self):
		return self._ClssfctnFinInstrm

	@ClssfctnFinInstrm.setter
	def ClssfctnFinInstrm(self, value):
		self._ClssfctnFinInstrm = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnFinInstrm', CFIOct2015Identifier, False)

	@ClssfctnFinInstrm.deleter
	def ClssfctnFinInstrm(self):
		del self._ClssfctnFinInstrm
		self._ClssfctnFinInstrm = base_types.UninitialisedField(self, 'ClssfctnFinInstrm', CFIOct2015Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnClssfctn', type=GenericIdentification86, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClssfctnFinInstrm', type=CFIOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
	))