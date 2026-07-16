# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentType2Code
from . import Max100KBinary

class EncapsulatedContent3(base_types._BaseFieldType):

	__slots__ = ["_Cntt", "_CnttTp"]
	@property
	def Cntt(self):
		return self._Cntt

	@Cntt.setter
	def Cntt(self, value):
		self._Cntt = value if value is not None else base_types.UninitialisedField(self, 'Cntt', Max100KBinary, False)

	@Cntt.deleter
	def Cntt(self):
		del self._Cntt
		self._Cntt = base_types.UninitialisedField(self, 'Cntt', Max100KBinary, False)

	@property
	def CnttTp(self):
		return self._CnttTp

	@CnttTp.setter
	def CnttTp(self, value):
		self._CnttTp = value if value is not None else base_types.UninitialisedField(self, 'CnttTp', ContentType2Code, False)

	@CnttTp.deleter
	def CnttTp(self):
		del self._CnttTp
		self._CnttTp = base_types.UninitialisedField(self, 'CnttTp', ContentType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cntt', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
	))