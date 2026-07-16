# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FundParameters5
from . import NoCriteria1Code

class FundParameters4Choice(base_types._BaseFieldType):

	__slots__ = ["_NoCrit", "_Params"]
	@property
	def NoCrit(self):
		return self._NoCrit

	@NoCrit.setter
	def NoCrit(self, value):
		self._NoCrit = value if value is not None else base_types.UninitialisedField(self, 'NoCrit', NoCriteria1Code, False)

	@NoCrit.deleter
	def NoCrit(self):
		del self._NoCrit
		self._NoCrit = base_types.UninitialisedField(self, 'NoCrit', NoCriteria1Code, False)

	@property
	def Params(self):
		return self._Params

	@Params.setter
	def Params(self, value):
		self._Params = value if value is not None else base_types.UninitialisedField(self, 'Params', FundParameters5, False)

	@Params.deleter
	def Params(self):
		del self._Params
		self._Params = base_types.UninitialisedField(self, 'Params', FundParameters5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoCrit', type=NoCriteria1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Params', type=FundParameters5, min=0, max=1, mutex_group=1, array=False),
	))