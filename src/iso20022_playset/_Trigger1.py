# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Document10
from . import FixedOrRecurrentDate1Choice

class Trigger1(base_types._BaseFieldType):

	__slots__ = ["_DcmntryEvt", "_DtChc"]
	@property
	def DcmntryEvt(self):
		return self._DcmntryEvt

	@DcmntryEvt.setter
	def DcmntryEvt(self, value):
		self._DcmntryEvt = value if value is not None else base_types.UninitialisedField(self, 'DcmntryEvt', Document10, True)

	@DcmntryEvt.deleter
	def DcmntryEvt(self):
		del self._DcmntryEvt
		self._DcmntryEvt = base_types.UninitialisedField(self, 'DcmntryEvt', Document10, True)

	@property
	def DtChc(self):
		return self._DtChc

	@DtChc.setter
	def DtChc(self, value):
		self._DtChc = value if value is not None else base_types.UninitialisedField(self, 'DtChc', FixedOrRecurrentDate1Choice, False)

	@DtChc.deleter
	def DtChc(self):
		del self._DtChc
		self._DtChc = base_types.UninitialisedField(self, 'DtChc', FixedOrRecurrentDate1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DcmntryEvt', type=Document10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtChc', type=FixedOrRecurrentDate1Choice, min=0, max=1, mutex_group=None, array=False),
	))