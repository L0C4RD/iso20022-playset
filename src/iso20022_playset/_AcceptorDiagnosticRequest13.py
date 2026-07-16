# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment81
from . import TrueFalseIndicator

class AcceptorDiagnosticRequest13(base_types._BaseFieldType):

	__slots__ = ["_AcqrrAvlbtyReqd", "_Envt"]
	@property
	def AcqrrAvlbtyReqd(self):
		return self._AcqrrAvlbtyReqd

	@AcqrrAvlbtyReqd.setter
	def AcqrrAvlbtyReqd(self, value):
		self._AcqrrAvlbtyReqd = value if value is not None else base_types.UninitialisedField(self, 'AcqrrAvlbtyReqd', TrueFalseIndicator, False)

	@AcqrrAvlbtyReqd.deleter
	def AcqrrAvlbtyReqd(self):
		del self._AcqrrAvlbtyReqd
		self._AcqrrAvlbtyReqd = base_types.UninitialisedField(self, 'AcqrrAvlbtyReqd', TrueFalseIndicator, False)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment81, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment81, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrAvlbtyReqd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
	))