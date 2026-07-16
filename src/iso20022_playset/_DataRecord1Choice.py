# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max10MbText
from . import Max20MbBinary

class DataRecord1Choice(base_types._BaseFieldType):

	__slots__ = ["_Binry", "_Txt"]
	@property
	def Binry(self):
		return self._Binry

	@Binry.setter
	def Binry(self, value):
		self._Binry = value if value is not None else base_types.UninitialisedField(self, 'Binry', Max20MbBinary, True)

	@Binry.deleter
	def Binry(self):
		del self._Binry
		self._Binry = base_types.UninitialisedField(self, 'Binry', Max20MbBinary, True)

	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if value is not None else base_types.UninitialisedField(self, 'Txt', Max10MbText, True)

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = base_types.UninitialisedField(self, 'Txt', Max10MbText, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Binry', type=Max20MbBinary, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Txt', type=Max10MbText, min=1, max=None, mutex_group=1, array=True),
	))