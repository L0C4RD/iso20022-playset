# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max52Text import Max52Text
from ._TrueFalseIndicator import TrueFalseIndicator

class PortfolioIdentification3(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_PrtflTxXmptn"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def PrtflTxXmptn(self):
		return self._PrtflTxXmptn

	@PrtflTxXmptn.setter
	def PrtflTxXmptn(self, value):
		self._PrtflTxXmptn = value if type(value) != base_types.auto else self.make_default("PrtflTxXmptn")

	@PrtflTxXmptn.deleter
	def PrtflTxXmptn(self):
		del self._PrtflTxXmptn
		self._PrtflTxXmptn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflTxXmptn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))