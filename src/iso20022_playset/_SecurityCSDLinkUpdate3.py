# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import TrueFalseIndicator

class SecurityCSDLinkUpdate3(base_types._BaseFieldType):

	__slots__ = ["_DfltLk", "_VldTo"]
	@property
	def DfltLk(self):
		return self._DfltLk

	@DfltLk.setter
	def DfltLk(self, value):
		self._DfltLk = value if value is not None else base_types.UninitialisedField(self, 'DfltLk', TrueFalseIndicator, False)

	@DfltLk.deleter
	def DfltLk(self):
		del self._DfltLk
		self._DfltLk = base_types.UninitialisedField(self, 'DfltLk', TrueFalseIndicator, False)

	@property
	def VldTo(self):
		return self._VldTo

	@VldTo.setter
	def VldTo(self, value):
		self._VldTo = value if value is not None else base_types.UninitialisedField(self, 'VldTo', DateAndDateTime2Choice, False)

	@VldTo.deleter
	def VldTo(self):
		del self._VldTo
		self._VldTo = base_types.UninitialisedField(self, 'VldTo', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DfltLk', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldTo', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))