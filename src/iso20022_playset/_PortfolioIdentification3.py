# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max52Text
from . import TrueFalseIndicator

class PortfolioIdentification3(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_PrtflTxXmptn"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Max52Text, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Max52Text, False)

	@property
	def PrtflTxXmptn(self):
		return self._PrtflTxXmptn

	@PrtflTxXmptn.setter
	def PrtflTxXmptn(self, value):
		self._PrtflTxXmptn = value if value is not None else base_types.UninitialisedField(self, 'PrtflTxXmptn', TrueFalseIndicator, False)

	@PrtflTxXmptn.deleter
	def PrtflTxXmptn(self):
		del self._PrtflTxXmptn
		self._PrtflTxXmptn = base_types.UninitialisedField(self, 'PrtflTxXmptn', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflTxXmptn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))