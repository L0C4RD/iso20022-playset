# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeMinimusApplicable1
from . import DeMinimusNotApplicable1

class DeMinimus1Choice(base_types._BaseFieldType):

	__slots__ = ["_DeMnmsAplbl", "_DeMnmsNotAplbl"]
	@property
	def DeMnmsAplbl(self):
		return self._DeMnmsAplbl

	@DeMnmsAplbl.setter
	def DeMnmsAplbl(self, value):
		self._DeMnmsAplbl = value if value is not None else base_types.UninitialisedField(self, 'DeMnmsAplbl', DeMinimusApplicable1, False)

	@DeMnmsAplbl.deleter
	def DeMnmsAplbl(self):
		del self._DeMnmsAplbl
		self._DeMnmsAplbl = base_types.UninitialisedField(self, 'DeMnmsAplbl', DeMinimusApplicable1, False)

	@property
	def DeMnmsNotAplbl(self):
		return self._DeMnmsNotAplbl

	@DeMnmsNotAplbl.setter
	def DeMnmsNotAplbl(self, value):
		self._DeMnmsNotAplbl = value if value is not None else base_types.UninitialisedField(self, 'DeMnmsNotAplbl', DeMinimusNotApplicable1, False)

	@DeMnmsNotAplbl.deleter
	def DeMnmsNotAplbl(self):
		del self._DeMnmsNotAplbl
		self._DeMnmsNotAplbl = base_types.UninitialisedField(self, 'DeMnmsNotAplbl', DeMinimusNotApplicable1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DeMnmsAplbl', type=DeMinimusApplicable1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DeMnmsNotAplbl', type=DeMinimusNotApplicable1, min=0, max=1, mutex_group=1, array=False),
	))