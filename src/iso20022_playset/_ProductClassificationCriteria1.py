# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CFIOct2015Identifier
from . import Max52Text

class ProductClassificationCriteria1(base_types._BaseFieldType):

	__slots__ = ["_ClssfctnFinInstrm", "_UnqPdctIdr"]
	@property
	def ClssfctnFinInstrm(self):
		return self._ClssfctnFinInstrm

	@ClssfctnFinInstrm.setter
	def ClssfctnFinInstrm(self, value):
		self._ClssfctnFinInstrm = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnFinInstrm', CFIOct2015Identifier, True)

	@ClssfctnFinInstrm.deleter
	def ClssfctnFinInstrm(self):
		del self._ClssfctnFinInstrm
		self._ClssfctnFinInstrm = base_types.UninitialisedField(self, 'ClssfctnFinInstrm', CFIOct2015Identifier, True)

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqPdctIdr', Max52Text, True)

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = base_types.UninitialisedField(self, 'UnqPdctIdr', Max52Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssfctnFinInstrm', type=CFIOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnqPdctIdr', type=Max52Text, min=0, max=None, mutex_group=None, array=True),
	))