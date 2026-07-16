# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class Acquirer7(base_types._BaseFieldType):

	__slots__ = ["_AcqrgInstn", "_Brnch"]
	@property
	def AcqrgInstn(self):
		return self._AcqrgInstn

	@AcqrgInstn.setter
	def AcqrgInstn(self, value):
		self._AcqrgInstn = value if value is not None else base_types.UninitialisedField(self, 'AcqrgInstn', Max35Text, False)

	@AcqrgInstn.deleter
	def AcqrgInstn(self):
		del self._AcqrgInstn
		self._AcqrgInstn = base_types.UninitialisedField(self, 'AcqrgInstn', Max35Text, False)

	@property
	def Brnch(self):
		return self._Brnch

	@Brnch.setter
	def Brnch(self, value):
		self._Brnch = value if value is not None else base_types.UninitialisedField(self, 'Brnch', Max35Text, False)

	@Brnch.deleter
	def Brnch(self):
		del self._Brnch
		self._Brnch = base_types.UninitialisedField(self, 'Brnch', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrgInstn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnch', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))