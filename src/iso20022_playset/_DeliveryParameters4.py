# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactIdentification2
from . import NameAndAddress4
from . import YesNoIndicator

class DeliveryParameters4(base_types._BaseFieldType):

	__slots__ = ["_CtctPrsn", "_NmAndAdr", "_RegdAdrInd"]
	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'CtctPrsn', ContactIdentification2, False)

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = base_types.UninitialisedField(self, 'CtctPrsn', ContactIdentification2, False)

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress4, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress4, False)

	@property
	def RegdAdrInd(self):
		return self._RegdAdrInd

	@RegdAdrInd.setter
	def RegdAdrInd(self, value):
		self._RegdAdrInd = value if value is not None else base_types.UninitialisedField(self, 'RegdAdrInd', YesNoIndicator, False)

	@RegdAdrInd.deleter
	def RegdAdrInd(self):
		del self._RegdAdrInd
		self._RegdAdrInd = base_types.UninitialisedField(self, 'RegdAdrInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdAdrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))