# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max15NumericText

class BinRange1(base_types._BaseFieldType):

	__slots__ = ["_HghrBin", "_LwrBin"]
	@property
	def HghrBin(self):
		return self._HghrBin

	@HghrBin.setter
	def HghrBin(self, value):
		self._HghrBin = value if value is not None else base_types.UninitialisedField(self, 'HghrBin', Max15NumericText, False)

	@HghrBin.deleter
	def HghrBin(self):
		del self._HghrBin
		self._HghrBin = base_types.UninitialisedField(self, 'HghrBin', Max15NumericText, False)

	@property
	def LwrBin(self):
		return self._LwrBin

	@LwrBin.setter
	def LwrBin(self, value):
		self._LwrBin = value if value is not None else base_types.UninitialisedField(self, 'LwrBin', Max15NumericText, False)

	@LwrBin.deleter
	def LwrBin(self):
		del self._LwrBin
		self._LwrBin = base_types.UninitialisedField(self, 'LwrBin', Max15NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HghrBin', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LwrBin', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))