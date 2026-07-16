# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MandateReason1Choice
from . import Max105Text
from . import YesNoIndicator

class AcceptanceResult6(base_types._BaseFieldType):

	__slots__ = ["_Accptd", "_AddtlRjctRsnInf", "_RjctRsn"]
	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if value is not None else base_types.UninitialisedField(self, 'Accptd', YesNoIndicator, False)

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = base_types.UninitialisedField(self, 'Accptd', YesNoIndicator, False)

	@property
	def AddtlRjctRsnInf(self):
		return self._AddtlRjctRsnInf

	@AddtlRjctRsnInf.setter
	def AddtlRjctRsnInf(self, value):
		self._AddtlRjctRsnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRjctRsnInf', Max105Text, True)

	@AddtlRjctRsnInf.deleter
	def AddtlRjctRsnInf(self):
		del self._AddtlRjctRsnInf
		self._AddtlRjctRsnInf = base_types.UninitialisedField(self, 'AddtlRjctRsnInf', Max105Text, True)

	@property
	def RjctRsn(self):
		return self._RjctRsn

	@RjctRsn.setter
	def RjctRsn(self, value):
		self._RjctRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctRsn', MandateReason1Choice, False)

	@RjctRsn.deleter
	def RjctRsn(self):
		del self._RjctRsn
		self._RjctRsn = base_types.UninitialisedField(self, 'RjctRsn', MandateReason1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRjctRsnInf', type=Max105Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RjctRsn', type=MandateReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))