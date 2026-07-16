# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Document9
from . import Max2000Text
from . import Undertaking9
from . import UndertakingTermination3

class UndertakingTerminationNotice1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_NclsdFile", "_TermntnDtls", "_UdrtkgId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if value is not None else base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@property
	def TermntnDtls(self):
		return self._TermntnDtls

	@TermntnDtls.setter
	def TermntnDtls(self, value):
		self._TermntnDtls = value if value is not None else base_types.UninitialisedField(self, 'TermntnDtls', UndertakingTermination3, False)

	@TermntnDtls.deleter
	def TermntnDtls(self):
		del self._TermntnDtls
		self._TermntnDtls = base_types.UninitialisedField(self, 'TermntnDtls', UndertakingTermination3, False)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TermntnDtls', type=UndertakingTermination3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
	))