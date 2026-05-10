import base_types
import Undertaking9
import Document9
import Max2000Text
import UndertakingTermination3

class UndertakingTerminationNotice1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_NclsdFile", "_TermntnDtls", "_UdrtkgId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	@property
	def TermntnDtls(self):
		return self._TermntnDtls

	@TermntnDtls.setter
	def TermntnDtls(self, value):
		self._TermntnDtls = value if type(value) != auto else self.make_default("TermntnDtls")

	@TermntnDtls.deleter
	def TermntnDtls(self):
		del self._TermntnDtls
		self._TermntnDtls = None

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if type(value) != auto else self.make_default("UdrtkgId")

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TermntnDtls', type=UndertakingTermination3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
	))

